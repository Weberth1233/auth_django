from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

class Tasks(models.Model):
    name_task = models.CharField(max_length=50) 
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        # Obtém os nomes dos usuários associados
        user_names = ', '.join(user.username for user in self.users.all())
        return f'{self.name_task} (Users: {user_names})'