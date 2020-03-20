# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from time import sleep

from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def sleeped(duration):
    sleep(duration)

@shared_task
def send_email_task():
    sleep(10)
    send_mail(
        'Subject here',
        'Here is the message.',
        'alexandrslot@gmail.com',
        ['anufriev.urich@gmail.com'],
        fail_silently=False,
    )