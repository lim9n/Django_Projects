from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def homepage(request):
      return render (request,'home.html')

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request,'show_tasks.html', {'tasks': tasks})  

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request,id):
    task = TaskModel.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_task.html', {'form': form})


def delete_task(request, id):
        task = TaskModel.objects.get(id=id)
        task.delete()
        return redirect('show_tasks')

def complete_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_task.html', {'completed_tasks': completed_tasks})

def complete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.is_completed = True
    task.save()    
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_task.html', {'completed_tasks': completed_tasks})

def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_task.html', {'completed_tasks': completed_tasks})

