from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from choreapi.views import HouseholdView, HouseholdMemberView, register_user, login_user, ChoresView, FeedView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'households', HouseholdView, 'household')
router.register(r'householdmembers', HouseholdMemberView, 'householdMember')
router.register(r'chores', ChoresView, 'chores' )
router.register(r'feed', FeedView, 'feed' )

urlpatterns = [
    path('', include(router.urls)),
     path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]

