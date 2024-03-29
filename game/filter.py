import django_filters
from .models import *

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'release_date']
