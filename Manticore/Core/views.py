from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    labels = ["January", "February", "March", "April"]
    data = [10, 20, 30, 40]

    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, "Core/dashboard.html", context)
