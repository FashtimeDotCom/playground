from celery import Celery
from random import randint

celery = Celery('tasks')
celery.config_from_object('.celeryconfig')





@celery.task
def xsum(numbers):
    return sum(numbers)
