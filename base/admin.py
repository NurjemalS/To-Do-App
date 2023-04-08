from django.contrib import admin
from .models import ToDoItem, Category

admin.site.register(ToDoItem)
admin.site.register(Category)
