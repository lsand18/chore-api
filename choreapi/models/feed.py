from django.db import models
from django.contrib.auth.models import User



class Feed(models.Model):
    name = models.CharField(max_length=50)
    servingsLeft = models.IntegerField()
    totalServings = models.IntegerField()
    url = models.CharField(max_length=100)