from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from todo.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo

# Create your views here.

class ListTodoAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer