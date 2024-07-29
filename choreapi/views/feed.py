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
        

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id','name',)