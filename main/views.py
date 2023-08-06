from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': "Main page", 'tasks': tasks})

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

def delete(request):
    pass