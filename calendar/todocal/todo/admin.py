from django.contrib import admin
from .models import Task, Category # , User

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
# admin.site.register(User)
