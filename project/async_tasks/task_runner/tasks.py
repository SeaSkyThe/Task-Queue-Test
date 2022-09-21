from huey.contrib.djhuey import periodic_task, task
from .signals import *
@task(retries=2, retry_delay=10)
def count_beans_task(number):
    print('-- Counted %s beans -- ' % number)
        
    return '-- Counted %s beans -- ' % number