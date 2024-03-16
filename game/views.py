from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Game
from .forms import GameForm


def index(request):
    games = Game.objects.all()
    return render(request, 'games/home.html', {'games': games})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

def game_create(request):
    form = GameForm(request.POST or None)
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_create = form.save()
            return redirect('index')
    else:
        form = GameForm()
    return render(request, 'games/game_form.html', {'form': form})

def game_update(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

def game_delete(request, pk):
    game = Game.objects.get(id=pk)
    game.delete()
    return render('index')

