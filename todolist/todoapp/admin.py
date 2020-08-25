from django.contrib import admin
from .models import Category,TodoList
# Register your models here.
admin.site.register(TodoList)
admin.site.register(Category)
