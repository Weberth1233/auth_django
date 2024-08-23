from rest_framework import serializers
from .models import Tasks, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']

class TaskSerializer(serializers.ModelSerializer):
    users = CustomUserSerializer(many=True, read_only=True)  # Inclui os detalhes dos usuários associados

    class Meta:
        model = Tasks
        fields = ['id', 'name_task', 'description', 'users']
