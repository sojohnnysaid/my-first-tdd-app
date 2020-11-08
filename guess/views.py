from django.shortcuts import render

# Create your views here.

def guess(request):
    return render(request, 'guess/guess.html')