from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.filter(task_status=False).order_by('-id')
    return render(request, 'main/index.html', {'title': "To Do List", 'tasks': tasks})

def done(request):
    tasks = Task.objects.filter(task_status=True).order_by('-done_date')
    return render(request, 'main/done.html', {'title': "Done List", 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Something went wrong'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = TaskForm(instance=task)
    return render(request, 'main/edit.html', {'form': form})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
    return redirect('home')

def do_undo(request, view, task_id):
    task = Task.objects.get(id=task_id)
    task.task_status = not task.task_status
    task.done_date = datetime.now()
    task.save()
    return redirect(view)


