from huey.contrib.djhuey import signal
from huey.signals import *

from async_tasks.settings import HUEY

@signal(SIGNAL_EXECUTING)
def task_signal_executing(signal, task):
    global HUEY
    HUEY.storage.put_data(f"{EXECUTING_PREFIX}-{task.id}", 1)

@signal(SIGNAL_COMPLETE)
def task_signal_complete(signal, task):
    global HUEY
    HUEY.storage.delete_data(f"{EXECUTING_PREFIX}-{task.id}")

@signal(SIGNAL_ERROR, SIGNAL_REVOKED)
def task_signal_error(signal, task, exc=None):
    global HUEY
    HUEY.storage.delete_data(f"{EXECUTING_PREFIX}-{task.id}")