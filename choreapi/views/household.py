from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Household

class HouseholdView(ViewSet):
    def create(self, request):

        household = Household()
        household.name = request.data['name']
        household.save()

        serialized = HouseholdSerializer(household, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
    

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ('name',)