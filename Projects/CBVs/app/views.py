from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView

from app import models

class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJCECTION'
        return context


class SchoolListView(ListView):
    # Model for listing all schools in the School model.
    # By default, it makes the items accessible in templates
    # using 'school_list' tag or whatever the
    # '(lowercase_model_class_name)_list' is.
    # To override the tag name, use 'context_object_name'
    # variable to rename the tag.

    context_object_name = 'schools' # Optional. Renamed tag to 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    # View about details about a specific school
    # By default, the tag name will be
    # '(lowercase_model_class_name)'

    context_object_name = 'school_detail' # Optional. Override tag name to 'school_detail'
    model = models.School
    template_name = "app/school_detail.html"