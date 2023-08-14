from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema

from .serializer import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo


def index(request):
    return HttpResponse('Страница приложения notes.')


class TodoListView(APIView):
    @swagger_auto_schema(
        operation_description="Get list of all todos.",
        responses={200: TodoSerializer(many=True)}
    )
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
