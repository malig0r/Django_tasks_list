from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')
    task_status = models.BooleanField('Done', default=False)
    done_date = models.DateField('Done on', default=timezone.now)

    def __str__(self):
        return self.title