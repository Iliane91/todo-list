from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(max_length=500)
    date = models.TimeField(null=True, blank=True, default='12:00:00')
    time = models.fields.IntegerField(null=True, blank=True,default='45')
    done = models.fields.BooleanField(default=False)

    def __str__(self):
        return self.name