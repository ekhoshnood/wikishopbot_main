from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print("request is POST")
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("request is not POST")
        context = {'form':form}
        return render(request, 'account/register.html', context)


def Login(request):
    return render(request, 'account/login.html')