from django.urls import include, path
from posts import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListClass.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("delete/<int:pk>/", views.DeletePost.as_view(), name="delete"),
    path("<username>/", views.UserPosts.as_view(), name="for_user"),
    path("<username>/<int:pk>/", views.PostDetail.as_view(), name="single") 
]
