from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task(name = "hello_Eugine")
def fun():
  print("hello Eugine")
  
