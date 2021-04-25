from django.shortcuts import render
from django.http import JsonResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    if request.method == 'GET':
        todos = TodoList.objects.all()
        print(type(todos[0].due))
        tasks = [("id : "+ str(i.id), "task name : "+i.task, "priority : "+ str(i.priority), "due date : " + str(i.due)) for i in todos]
        return JsonResponse({"task list" : tasks})
    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoListSerializer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print(request.data['id'])
        print(type(request.data['id']))
        todos = TodoList.objects.get(id=request.data['id'])
        TodoList.objects.filter(id=request.data['id']).delete()
        return JsonResponse({"deleted":["id : "+str(todos.id), "task : "+todos.task, "priority : "+str(todos.priority), "due data : "+str(todos.due)]})
