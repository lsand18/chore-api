from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .household import Household
from .feed import Feed


class Chore(models.Model):
    name = models.CharField(max_length=50)
    # frequency = models.IntegerField(validators=[MinValueValidator(1)],null=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name="choreHousehold")
    feed = models.ForeignKey(Feed, on_delete=models.DO_NOTHING, null=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)