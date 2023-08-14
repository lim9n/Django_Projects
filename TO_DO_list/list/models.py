from django.db import models

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=30,verbose_name="Task Title")
    taskDescription = models.TextField(verbose_name="Task Description")
    is_completed = models.BooleanField(default=False, verbose_name="Is Completed")

 
