from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Game
from .forms import GameForm, SignUpForm
from .filter import GameFilter


# signup page
def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created' )
            return redirect('login')
    
    return render(request, 'auth/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, e.g., home page
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

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

