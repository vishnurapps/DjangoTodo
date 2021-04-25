from django.db import models

# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=255)
    priority = models.IntegerField()
    due = models.DateField()
