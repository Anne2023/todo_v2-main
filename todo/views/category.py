from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.category import CategoryEntity
from todo.serializers.category import CategorySerializer


class CategoryView(APIView):
    """
    Hello Guys
    """
    def get(self, request, format=None):
        categories = CategoryEntity.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

