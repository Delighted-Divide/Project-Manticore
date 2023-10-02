from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="Dashboard"),
    path('register', views.register, name="Register")
]
