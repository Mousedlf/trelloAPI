from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from app.api.serializers import ListSerializer, BoardSerializer, CardSerializer
from app.models import List, Board, Card


# BOARDS _______________________________________________________________________________________

@api_view(['GET'])
def index_boards(request):
    board = Board.objects.all()
    serialized_boards = BoardSerializer(board, many=True)

    return Response(serialized_boards.data)


@api_view(['POST'])
def new_board(request):
    if request.method == 'POST':
        board = Board()
        serialized_board = ListSerializer(instance=board, data=request.data)
        if serialized_board.is_valid():
            serialized_board.save()
            return Response(serialized_board.data, status=status.HTTP_201_CREATED)

    return Response("try again", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show_board(request, id):
    board = Board.objects.get(id=id)
    serialized_board = BoardSerializer(board, many=False)
    return Response(serialized_board.data)


@api_view(['POST'])
def edit_board(request, id):
    board = Board.objects.get(id=id)
    if request.method == 'POST':
        serialized_board = BoardSerializer(instance=board, data=request.data)
        if serialized_board.is_valid():
            serialized_board.save()
            return Response("board changes saved")


@api_view(['DELETE'])
def delete_board(request, id):
    Board.objects.filter(id=id).delete()
    return Response("bye bye board")


# LISTS ________________________________________________________________________________________

@api_view(['POST'])
def new_list(request,id):
    board = Board.objects.get(id=id)
    if board is None:
        return Response("no board")

    if request.method == 'POST':
        list = List()
        serialized_list = ListSerializer(instance=list, data=request.data)

        if serialized_list.is_valid():
            serialized_list.save(board=get_object_or_404(Board, id=id))

            return Response("new list created")


@api_view(['POST'])
def edit_list(request,id):
    list = List.objects.get(id=id)
    if list is None:
        return Response("no such list") # ne fonctionne pas

    if request.method == 'POST':
        serialized_list = ListSerializer(instance=list, data=request.data)
        if serialized_list.is_valid():
            serialized_list.save()
            return Response("list changes saved")


@api_view(['DELETE'])
def delete_list(request,id):
    List.objects.filter(id=id).delete()
    return Response("list deleted")


# CARDS ________________________________________________________________________________________
@api_view(['POST'])
def new_card(request, id):
    list = List.objects.get(id=id)
    if list is None:
        return Response("no list")

    if request.method == 'POST':
        card = Card()
        serialized_card = CardSerializer(instance=card, data=request.data)

        if serialized_card.is_valid():
            serialized_card.save(list=get_object_or_404(List, id=id))

            return Response("card created")


@api_view(['POST'])
def edit_card(request, id):
    card = Card.objects.get(id=id)
    # verif si carte existe bien
    if request.method == 'POST':
        serialized_card = CardSerializer(instance=card, data=request.data)
        if serialized_card.is_valid():
            serialized_card.save()
            return Response("card changes saved")


@api_view(['DELETE'])
def delete_card(request, id):
    Card.objects.filter(id=id).delete()
    return Response("card deleted")