from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from choreapi.models import Feed


class FeedView(ViewSet):
    def create(self, request):

        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('name',)