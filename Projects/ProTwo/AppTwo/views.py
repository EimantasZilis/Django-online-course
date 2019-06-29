from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users

def index_page(request):
    return HttpResponse(r"<em>My second app </em>")

def help_page(request):
    mappings = {"help_txt": "How can I help you today?"}
    return render(request, 'AppTwo/help.html', context=mappings)

def users_page(request):
    users_list = Users.objects.order_by('id')
    users_dict = {'users': users_list}
    return render(request, 'AppTwo/users.html', context=users_dict)
