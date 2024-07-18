from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from choreapi.views import HouseholdView, HouseholdMemberView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'households', HouseholdView, 'household')
router.register(r'householdmembers', HouseholdMemberView, 'householdMember')

urlpatterns = [
    path('', include(router.urls)),
]

