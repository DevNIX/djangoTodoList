from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    tasklist = models.ForeignKey('List', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)


class List(models.Model):

    owner = models.ForeignKey(User, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    @classmethod
    def get_list_and_task(self, _owner=None):
        if _owner is None:
            return self.objects.select_related('task_set').all()
        else:
            return self.objects.select_related('task_set').filter(owner=_owner)
