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
<<<<<<< HEAD
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password,', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password,', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
=======
>>>>>>> 35719fdd13481954c13b5cbf9d564d27e27b852f

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

<<<<<<< HEAD
=======
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
>>>>>>> 35719fdd13481954c13b5cbf9d564d27e27b852f
