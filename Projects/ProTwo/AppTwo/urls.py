from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^users', views.users_page, name='users'),
    url(r'^index', views.index_page, name='index'),
    url(r'^help/', views.help_page, name="help")
]
