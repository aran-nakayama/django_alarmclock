from django.db import models

# Create your models here.
class TimeModel(models.Model):
    hour = models.CharField(max_length=10)
    minute = models.CharField(max_length=10)