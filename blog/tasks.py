from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

@shared_task(name = "hello_world")
def fun():
  print("hello Eugine")
  
