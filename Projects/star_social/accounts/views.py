from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm

    # Redirect them to login page upon successful sign up
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
