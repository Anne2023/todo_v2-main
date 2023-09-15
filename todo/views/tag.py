from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.tag import TagEntity
from todo.serializers.tag import TagSerializer

class TagView(APIView):
    """
    List all tags, or create a new tag.
    """
def get_task(self, pk):
    	pass
        
def get(self, request, format=None):
    	pass

def post(self, request, format=None):
    	pass
