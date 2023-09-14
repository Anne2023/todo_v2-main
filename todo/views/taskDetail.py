from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity
from todo.serializers.task import TaskSerializer

class TaskDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_task(self, pk):
        try:
            return TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_task(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass