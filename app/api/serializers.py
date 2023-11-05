from rest_framework.serializers import ModelSerializer
from app.models import Card, List, Board


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ["id","content"]


class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = ["id", "name", "cards"]
    cards = CardSerializer(many=True, required=False)


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "name", "lists"]
    lists = ListSerializer(many=True, required=False)




