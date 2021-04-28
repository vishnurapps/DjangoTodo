from rest_framework import serializers 
from .models import TodoList
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    todolist = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoList.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todolist']
  
class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
 
    class Meta:
        model = TodoList
        fields = ('id',
                  'task',
                  'priority',
                  'due',
                  'owner')