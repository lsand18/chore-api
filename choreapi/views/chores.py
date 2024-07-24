from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Chore, Household

class ChoresView(ViewSet):
    def create(self, request):

        chore = Chore()
        chore.name = request.data['name']
        chore.household = Household.objects.get(pk=request.data['householdId'])
        chore.save()

        serialized = ChoreSerializer(chore, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
 
    
    def list(self, request):
        householdId = self.request.query_params.get('household', None)
        chores = Chore.objects.filter(household=householdId)
        json_chores = ChoreSerializer(
            chores, many=True, context={'request': request}
        )
        return Response(json_chores.data)
    
    # def list(self, request):
    #     householdId = self.request.query_params.get('household', None)
    #     chores = Chore.objects.filter(household=householdId)
    #     json_chores = ChoreSerializer(
    #         chores, many=True, context={'request': request}
    #     )
    #     return Response(json_chores.data)
class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chore
        fields = ('id','name',)