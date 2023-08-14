from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
      
      path('',views.homepage,name="homepage"),
      path('add/', views.add_task, name='add_task'),
      path('show_task/',views.show_tasks,name='show_tasks'),
      path('delete_task/<int:id>',views.delete_task,name='delete_task'),
      path('edit_task/<int:id>',views.edit_task,name='edit_task'),
      path('completed_tasks', views.completed_tasks, name='completed_tasks'),
      path('complete_task/<int:id>/', views.complete_task, name='complete_task'),



]

