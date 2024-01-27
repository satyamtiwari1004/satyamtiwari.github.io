
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_home),
    path('data', views.load_data),
]