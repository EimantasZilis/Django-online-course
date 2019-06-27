from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return HttpResponse(r"<em>My second app </em>")
