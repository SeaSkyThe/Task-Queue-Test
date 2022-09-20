from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('tasks/', views.count_beans, name='count_beans'),
]