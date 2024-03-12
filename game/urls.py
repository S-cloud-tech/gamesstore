from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('new/', views.game_create, name='game_create'),
    path('<int:pk>/edit/', views.game_update, name='game_update'),
    path('<int:pk>/delete/', views.game_delete, name='game_delete'),
]
