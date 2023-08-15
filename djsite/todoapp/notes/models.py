from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    not_done = models.BooleanField(default=False)
    in_process = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
