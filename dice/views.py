from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'dice/start.html')

def game(request):
    return render(request, 'dice/game.html')