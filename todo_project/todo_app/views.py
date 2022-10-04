from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import Todoform

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.

def home(request):
    task1 = Task.objects.all()
    dictionary = {'task': task1}

    if request.method == "POST":
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'home.html', dictionary)

def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')

def update(request, id):
    task = Task.objects.get(id=id)
    form = Todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task, 'form': form})

# class based views

class Task_listview(ListView):

    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class Task_detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Task_updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todo_app:cbvdetail', kwargs={'pk': self.object.id})


class Task_deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:cbvhome')