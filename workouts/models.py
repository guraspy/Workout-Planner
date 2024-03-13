from django.db import models
from django.contrib.auth import get_user_model
from exercises.models import Exercise

User = get_user_model()

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    frequency = models.PositiveIntegerField()
    goal = models.CharField(max_length=255)
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField()