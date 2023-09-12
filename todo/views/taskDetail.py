from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.task import TaskEntity
from todo.serializers.task import TaskSerializer


class TaskDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk):
        pass

    def get(self, request, pk, format=None):
        tasks = TaskEntity.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass
    