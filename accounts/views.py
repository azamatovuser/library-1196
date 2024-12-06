from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_function(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #username and password
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register_function(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST) #username, password and truth password
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)