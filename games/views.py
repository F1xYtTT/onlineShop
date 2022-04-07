from django.shortcuts import render
from django.views.generic import ListView, DetailView
from games.models import Game

class GameListView(ListView):
    model = Game
    template_name = 'games/home.html'
    context_object_name = 'game_list'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'




def home(request):
    return render(request,'home.html')

