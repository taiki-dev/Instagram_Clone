from django.shortcuts import render

from djagno.views.generic import ListView, CreateView
from djanog.urls import reverse_lazy
from .models import PostModel

class ListClass(ListView):
    template_name = 'list.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'form.html'
    model = PostModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')