from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):

    context = {
        'pname': "Dashboard"
    }
    return render(request, "dashboard.html", context)
