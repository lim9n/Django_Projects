from django.contrib import admin
from list.models import TaskModel
# Register your models here.


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'is_completed')

admin.site.register(TaskModel, TaskModelAdmin)