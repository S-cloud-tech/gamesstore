from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    genre = forms.CharField(required=True)
    game_pic = forms.ImageField(required=True)
    release_date = forms.DateField()
    price = forms.IntegerField()
    class Meta:
        model = Game
        fields = ['title', 'description', 'genre', 'game_pic', 'release_date', 'price']

