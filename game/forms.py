from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control', 'data-toggle':'password', 'id':'password'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control', 'data-toggle':'password', 'id':'password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

