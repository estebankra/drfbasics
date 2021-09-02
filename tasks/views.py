# Django Rest Framework
from rest_framework import viewsets
# Models
from .models import Tasks
# Serializer
from .serializers import TasksModelSerializer


class TasksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing tasks.
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksModelSerializer
