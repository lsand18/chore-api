from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from choreapi.views import HouseholdView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'households', HouseholdView, 'household')

urlpatterns = [
    path('', include(router.urls)),
]

