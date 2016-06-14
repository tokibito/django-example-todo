from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    if request.GET.get('all') == '1':
        queryset = Todo.objects.all()
    else:
        queryset = Todo.objects.filter(done=False)
    todo_list = queryset.order_by('-created_at')
    return render(request, 'index.html', {'todo_list': todo_list})

def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add.html', {'form': form})

def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'edit.html', {'form': form})

def done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = True
    todo.save()
    return redirect('index')
