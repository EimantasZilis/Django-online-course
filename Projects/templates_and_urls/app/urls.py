from django.urls import path
from app import views

# Template tagging: it must have app_name variable name.
# The string must represent app name
app_name = "app"

urlpatterns = [
    path('relative/', views.relative, name="relative"),
    path("other/", views.other, name="other")
]