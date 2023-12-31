from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # index
    path('', views.documentation),
    path('boards/', views.index_boards),
    path('users/', views.index_users),
    # boards
    path('new/board/', views.new_board),
    path('board/<str:id>/', views.show_board),
    path('edit/board/<str:id>/', views.edit_board),
    path('delete/board/<str:id>/', views.delete_board),
    # lists
    path('new/list/board/<str:id>/', views.new_list),
    path('edit/list/<str:id>/', views.edit_list),
    path('delete/list/<str:id>/', views.delete_list),
    # cards
    path('new/card/list/<str:id>/', views.new_card),
    path('edit/card/<str:id>/', views.edit_card),
    path('delete/card/<str:id>/', views.delete_card),
    # labels
    path('new/label/board/<str:id>/', views.new_label),
    # user
    path('register/', views.register),


]