from django.shortcuts import render
from AppTwo.forms import NewUserForm

def index_page(request):
    return render(request, 'AppTwo/index.html')

def help_page(request):
    mappings = {"help_txt": "How can I help you today?"}
    return render(request, 'AppTwo/help.html', context=mappings)

def users_page(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_page(request)
        else:
            print("ERROR: form invalid")
    return render(request, 'AppTwo/users.html', context={'form': form})
