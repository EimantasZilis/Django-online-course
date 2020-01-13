from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm

    # Redirect them to login page upon successful sign up
    success_url = reverse_lazy('login')

    # Note that signup.html is in registration folder, not in accounts
    # which is the app name! This is because django's built-in views
    # expect login/singup templates to be in registration folder.
    template_name = 'registration/signup.html'
