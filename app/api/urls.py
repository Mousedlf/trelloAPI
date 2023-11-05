from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_boards),
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

]