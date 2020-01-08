from django.urls import path, re_path
from app import views

app_name = 'app'

# Specifying the name against each path allows that view
# to be referenced in the templates. 
# # E.g. name='list' allows {% url 'app:list' %} to work 

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail')
]