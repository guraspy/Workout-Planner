from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=255)
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(default=0.0)