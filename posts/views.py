from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from django.contrib.auth.mixins import LoginRequiredMixin

class ListClass(ListView):
    template_name = 'index.html'
    model = PostModel

class FormClass(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    model = PostModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)