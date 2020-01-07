from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from app.forms import UserForm, UserProfileInfoForm

def index(request):
    return render(request, 'app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # Save user_form directory to database. Why?
            user.set_password(user.password)  # Hash password
            user.save() # Save to database

            profile = profile_form.save(commit=False) # Save to database, don't commit yet
            profile.user = user # Set up one-to-one relationship with user (in the views)

            if 'profile_pic' in request.FILES:
                # Put uploaded picture against profile model
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    mappings = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'app/registration.html', mappings)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Someone tried to log in and failed")
            print(f' >> Username: {username} and password: {password}')
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, "app/login.html", {})