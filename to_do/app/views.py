from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app/index.html', {'tasks': tasks})


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


def task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    if not task.completed:
        task.completed = True
        task.save()
    return redirect('task_list')

