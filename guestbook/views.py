from django.shortcuts import render

# Create your views here.

def guestbook(request):
    return render(request, 'guestbook/guestbook.html')