from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group




class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'  # Choose a unique related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'  # Choose a unique related_name
    )
    def __str__(self):
        return self.username

   


class Question(models.Model):
    OPTIONS = [
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'),
        ('option_3', 'Option 3'),
        ('option_4', 'Option 4'),
    ]

    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255, choices=OPTIONS)

    def __str__(self):
        return self.question
