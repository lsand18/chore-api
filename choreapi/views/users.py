from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from django.db.models import Q
from choreapi.models import HouseholdMember

class UserView(ViewSet):

    def list(self, request):
        search_text = self.request.query_params.get('q', None)
        if search_text:
            all_users =User.objects.filter(
                Q(first_name__contains=search_text) |
                Q(last_name__contains=search_text))
            currentHouseholdId = self.request.query_params.get('household')
            excluded_users = HouseholdMember.objects.filter(household = currentHouseholdId)
            excluded_user_ids = excluded_users.values_list('user_id')
            users = all_users.exclude(id__in=excluded_user_ids)
        else:
            users = None
        user_data = UserSerializer(
            users, many=True, context={'request': request}
        )
        return Response(user_data.data)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name')