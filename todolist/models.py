from django.db import models

# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=255)
    priority = models.IntegerField()
    due = models.DateField()

    owner = models.ForeignKey('auth.User', related_name='todolist', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(TodoList, self).save(*args, **kwargs)
