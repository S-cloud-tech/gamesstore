from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
from .filter import GameFilter


def game_index(request):
    if 'f' in request.GET:
        f = request.GET['f']
        games = Game.objects.filter(title__icontains=f)
    else:
        games = Game.objects.all()
    gamefilter = GameFilter()
    context = {'games': games, 'gamefilter':gamefilter}
    return render(request, 'games/home.html', context)

def game_list(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games/game_list.html', context)

def game_detail(request, pk):
    games = Game.objects.get(pk=pk)
    context = {'games': games}
    return render(request, 'games/game_detail.html', context)

def add_game(request):
    form = GameForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'games/add_game.html', context)

def edit_game(request, pk):
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'games/add_game.html', context)

def delete_game(request, pk):
    game = Game.objects.get(id=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('/')
    return render(request, 'games/game_confirm_delete.html', {'game': game})

