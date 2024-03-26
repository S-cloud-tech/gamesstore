from django.urls import path
from . import views

urlpatterns = [
    #Authentication
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),


    path('home/', views.game_index, name='home'),
    path('', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('add/', views.add_game, name='add_game'),
    path('<str:pk>/edit/', views.edit_game, name='edit_game'),
    path('<str:pk>/delete/', views.delete_game, name='delete_game'),
]
