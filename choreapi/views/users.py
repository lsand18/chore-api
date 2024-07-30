from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from django.db.models import Q

class UserView(ViewSet):

    def list(self, request):
        search_text = self.request.query_params.get('q', None)
        users =User.objects.filter(
            Q(first_name__contains=search_text) |
            Q(last_name__contains=search_text)
)
        user_data = UserSerializer(
            users, many=True, context={'request': request}
        )
        return Response(user_data.data)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name')