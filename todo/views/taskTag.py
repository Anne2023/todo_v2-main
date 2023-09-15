from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.serializers.taskTag import TaskTagSerializer

class TaskTagView(APIView):
    """
    Associate task and tags.
    """        
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass