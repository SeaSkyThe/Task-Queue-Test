from django.shortcuts import render

# Create your views here.
from huey.contrib.djhuey import periodic_task, task

@task()
def count_beans(number):
    print('-- Counted %s beans -- ' % number)
    return ('-- Counted %s beans -- ' % number)