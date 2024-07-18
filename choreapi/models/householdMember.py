from django.db import models
from django.contrib.auth.models import User
from .household import Household

class HouseholdMember(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="householdUser")
    household = models.ForeignKey(Household, on_delete=models.DO_NOTHING, related_name="userHousehold")

   