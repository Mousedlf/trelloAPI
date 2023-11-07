from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = "username"


class Board(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="lists", null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Label(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="labels", null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    content = models.CharField(max_length=1000)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="cards", null=True)
    label = models.ForeignKey(Label, null=True, on_delete=models.SET_NULL)











