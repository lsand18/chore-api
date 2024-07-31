from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Feed, Household


class FeedView(ViewSet):

    def create(self, request):

        newFeed = Feed()
        newFeed.name = request.data['name']
        newFeed.household = Household.objects.get(pk=request.data['householdId'])
        newFeed.url = request.data['url']
        newFeed.save()

        serialized = FeedSerializer(newFeed, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        householdId = self.request.query_params.get('household', None)
        feed = Feed.objects.filter(household=householdId)
        json_feed = FeedSerializer(
            feed, many=True, context={'request': request}
        )
        return Response(json_feed.data)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single payment type

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            void = Feed.objects.get(pk=pk)
            void.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Feed.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id','name','url')