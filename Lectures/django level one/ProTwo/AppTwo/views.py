from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    return HttpResponse(r"<em>My second app </em>")

def help_page(request):
    mappings = {"help_txt": "How can I help you today?"}
    return render(request, 'AppTwo/help.html', context=mappings)
