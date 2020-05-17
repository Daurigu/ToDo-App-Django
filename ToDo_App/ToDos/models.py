from django.db import models
from django import utils

# Create your models here.

class Todo(models.Model):
    date = models.DateTimeField(default = utils.timezone.now)
    text = models.CharField(max_length = 200)