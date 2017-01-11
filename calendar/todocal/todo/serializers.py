from .models import Task, Category, User
from rest_framework import serializers

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
