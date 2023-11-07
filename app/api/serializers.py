from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app.models import Card, List, Board, Label, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]  # id, password

    def validate_password(self, value: str) -> str:
        return make_password(value)


class LabelSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields = ["id","name"]


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "content", "label"]
    label = LabelSerializer(required=False)


class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = ["id", "creator", "name", "cards"]
    cards = CardSerializer(many=True, required=False)
    creator = UserSerializer(read_only=True)


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "creator", "created", "name", "labels", "lists"]
    lists = ListSerializer(many=True, required=False)
    labels = LabelSerializer(read_only=True, many=True)
    creator = UserSerializer(read_only=True)





