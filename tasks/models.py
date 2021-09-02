# Django
from django.db import models


class Tasks(models.Model):
    """
    Tasks models
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
