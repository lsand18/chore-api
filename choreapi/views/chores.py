from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Chore, Household, Feed

class ChoresView(ViewSet):
    def create(self, request):

        chore = Chore()
        chore.name = request.data['name']
        chore.household = Household.objects.get(pk=request.data['householdId'])
        if request.data['feedId']:
            chore.feed = Feed.objects.get(pk=request.data['feedId'])
        else:
            chore.feed = None
        chore.save()

        serialized = ChoreSerializer(chore, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        chore = Chore.objects.get(pk=pk)
        json_chore = ChoreSerializer(chore, many=False)
        return Response(json_chore.data)
 
    
    def list(self, request):
        householdId = self.request.query_params.get('household', None)
        chores = Chore.objects.filter(household=householdId)
        json_chores = ChoreSerializer(
            chores, many=True, context={'request': request}
        )
        return Response(json_chores.data)
    
    def update(self, request, pk=None):
        if request.data:
            chore = Chore.objects.get(pk=pk)
            chore.name = request.data["name"]
            if request.data['feed']:
                feed_data = request.data.get('feed', {})
                feedId = feed_data.get('id')
                feed = Feed.objects.get(pk=feedId)
                chore.feed = feed
            else: 
                chore.feed = None
            chore.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        else:
            chore = Chore.objects.get(pk=pk)
            chore.complete = not chore.complete
            if chore.user:
                chore.user = None
            else:
                chore.user = request.auth.user
            chore.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single payment type

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            void = Chore.objects.get(pk=pk)
            void.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Chore.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chore
        fields = ('id','name','complete', 'feed', 'user')
        depth = 2