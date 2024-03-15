from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm


def index(request):
    return render(request, 'games/home.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
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
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})

