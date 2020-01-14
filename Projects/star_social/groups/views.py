from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # Users shouldn't be able to edit fields like slug or description_html
    fields = ("name", "description")
    model = Group


class SingleGroup(generic.DetailView):
    # For viewing single group
    model = Group


class ListGroups(generic.ListView):
    # For viewing multiple groups
    model = Group
