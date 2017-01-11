from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True) # Task.objects.all().order_by('-date') to order in chronological order
    # reminder = foreign key

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    # reminder
    # we need a default category

    def __str__(self):
        return self.title

# more models to add?
