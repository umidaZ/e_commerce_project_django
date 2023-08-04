from django.shortcuts import render
from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy
# Create your views here.

class SignUp(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')