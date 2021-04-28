from django.shortcuts import render
from django.http import JsonResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def all(request):
    if request.method == 'GET':
        todos = TodoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        todo_serializer = TodoListSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


