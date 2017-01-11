from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Category, User
from .serializers import TaskSerializer, CategorySerializer, UserSerializer
from .forms import TaskForm, CategoryForm

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date')
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
