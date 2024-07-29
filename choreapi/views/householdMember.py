from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import HouseholdMember, Household
from django.contrib.auth.models import User

class HouseholdMemberView(ViewSet):
    def create(self, request):
# """ http://localhost:8000/householdmembers"""
# TODO: create try/except so a member cannot be added to a household twice
        newMember = HouseholdMember()
        newMember.user = User.objects.get(pk = request.data['chosenId'])
        newMember.household = Household.objects.get(pk = request.data['householdId'])
        newMember.save()

        serialized = HouseholdMemberSerializer(newMember, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        householdId = self.request.query_params.get('household', None)
        houseMembers = HouseholdMember.objects.filter(household=householdId)
        json = HouseholdMemberSerializer(
            houseMembers, many=True, context={'request': request}
        )
        return Response(json.data)
    
    def destroy(self, request, pk=None):
        """ http://localhost:8000/householdmembers/pk"""
        try:
            void = HouseholdMember.objects.get(pk=pk)
            if void.user.id != request.auth.user.id:
                void.delete()
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'You cannot remove yourself from the household.'}, status=status.HTTP_403_FORBIDDEN)
        except HouseholdMember.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

class HouseholdMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdMember
        fields = ('id','user','household')
        depth = 2