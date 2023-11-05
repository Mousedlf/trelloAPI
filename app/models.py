from django.contrib.auth.models import AbstractUser
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)


class List(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="lists", null=True)


class Card(models.Model):
    content = models.CharField(max_length=1000)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="cards", null=True)





