from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Todo

# Create your views here.

class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
       model = Todo
       fields = ['title', 'deadline']
       success_url = reverse_lazy('todo_list')