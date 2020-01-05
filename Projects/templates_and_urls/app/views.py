from django.shortcuts import render

def index(request):
    context_dict = {'text': 'hello world', 'number':100}
    return render(request, "app/index.html", context_dict)
 
def other(request):
    return render(request, "app/other.html")

def relative(request):
    return render(request, "app/relative_url_templates.html")