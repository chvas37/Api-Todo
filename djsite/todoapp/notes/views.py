from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema

from .serializer import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo


class TodoListView(APIView):
    @swagger_auto_schema(
        operation_description="Get list of all todos.",
        responses={200: TodoSerializer(many=True)}
    )
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        post_new = Todo.objects.create(
            title=request.data['title'],
            description=request.data['description']
        )
        # serializer = TodoSerializer(post_new)
        return Response({'post': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Todo.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TodoSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method DELETE not allowed"})

        return Response({'post': "delete post" + str(pk)})