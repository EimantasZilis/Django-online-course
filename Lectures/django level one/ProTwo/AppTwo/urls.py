from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^index', views.index_page, name='index'),
    url(r'^help/', views.help_page, name="help")
]
