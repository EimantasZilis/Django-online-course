from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views


app_name = 'accounts'

# Note that login.html is in registration folder, not in accounts
# which is the app name! This is because django's built-in views
# expect login/singup templates to be in registration folder.
urlpatterns = [
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]