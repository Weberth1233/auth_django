from django.contrib import admin
from .models import *
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','bio')
    search_fields = ('username', 'email')

class TasksAdmin(admin.ModelAdmin):
    list_display = ('name_task', 'description')
    search_fields = ('name_task', 'description')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tasks, TasksAdmin)