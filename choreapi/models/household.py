from django.db import models


class Household(models.Model):

    title = models.CharField(max_length=15)
   