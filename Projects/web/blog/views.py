from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from blog forms import PostForm, CommentForm
from blog.models import Post, Comment


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # Do a query on your model. Get post model
        # and all the objects there. Filter out
        # based on given conditions. This example
        # returns posts that were published <= now
        # and sorts by published date.
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')


class PostDetailView(DetaiView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # LoginRequiredMixin fields
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'


class PostDeleteView(LoginRequiredMixing, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__isnull=True
        ).order_by('created_date')


