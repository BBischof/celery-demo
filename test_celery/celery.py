from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://bryan:bryanpass@localhost/bryan_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
