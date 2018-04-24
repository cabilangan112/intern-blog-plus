from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.views.generic import (ListView,DetailView,UpdateView,CreateView)
# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'

    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)