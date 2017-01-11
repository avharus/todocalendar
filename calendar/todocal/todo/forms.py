from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
        
