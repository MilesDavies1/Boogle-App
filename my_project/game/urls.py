# game/urls.py

from django.urls import path
from .views import WordsView, SavedGameView, home

urlpatterns = [
    path('', home, name='home'),  # This will handle the empty path '/'
    path('api/words/', WordsView.as_view(), name='words_list'),
    path('api/save_game/', SavedGameView.as_view(), name='save_game'),
    path('api/saved_games/', SavedGameView.as_view(), name='saved_games_list'),
]

