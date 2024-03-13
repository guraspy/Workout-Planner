from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desired_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)