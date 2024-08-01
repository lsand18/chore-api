from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Household, HouseholdMember
from django.contrib.auth.models import User

class HouseholdView(ViewSet):
    def create(self, request):

        household = Household()
        household.name = request.data['name']
        household.save()

        newMember = HouseholdMember()
        newMember.user = request.auth.user
        newMember.household = household
        newMember.save()

        serialized = HouseholdSerializer(household, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        households = HouseholdMember.objects.filter(user=request.auth.user)
        json_households = HouseholdMemberSerializer(
        households, many=True, context={'request': request})
        return Response(json_households.data)
    
    def retrieve(self, request, pk=None):
        try:
            household = Household.objects.get(pk=pk)
        except:
            household = None
        json_household = HouseholdSerializer(household, many=False)
        return Response(json_household.data)
    

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ('id','name',)

class HouseholdMemberSerializer(serializers.ModelSerializer):
    household = HouseholdSerializer(many=False)
    class Meta:
        model = HouseholdMember
        fields = ('id', 'household')