from django.db import models
from datetime import datetime

# Create your models here.

class TotalViewsModel(models.Model):
    label = models.CharField(max_length=64)
    views = models.IntegerField()

class MostWatchedVideos(models.Model):
    title = models.CharField(max_length=64)
    published_date = models.DateTimeField(default=datetime.now())
    views_count = models.IntegerField(default=0)