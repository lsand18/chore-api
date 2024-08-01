from django.db import models
from .household import Household


class Feed(models.Model):
    name = models.CharField(max_length=50)
    servingsLeft = models.IntegerField(null=True)
    totalServings = models.IntegerField(null=True)
    url = models.CharField(max_length=100)
    household = models.ForeignKey(Household, on_delete=models.DO_NOTHING, related_name="feedHousehold")