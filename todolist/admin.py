from django.contrib import admin

from .models import TodoList

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('task', 'priority', 'due')

# Register your models here.

admin.site.register(TodoList, TodoListAdmin)

