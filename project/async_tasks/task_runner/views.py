from django.shortcuts import render
from django.http import HttpResponse
from .tasks import count_beans_task
from .signals import *
# Create your views here.

def count_beans(request, beans):
    for i in range(0, 50):
        result = count_beans_task(beans)
    return HttpResponse(result.get(blocking=True, preserve=True))