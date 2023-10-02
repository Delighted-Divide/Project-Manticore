from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.


def dashboard(request):
    context = {'pname': "Dashboard"}
    return render(request, "dashboard.html", context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
        print("Input", form)
    return render(request, 'register.html', {'form': form, 'pname': "Register"})
