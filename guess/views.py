from django.shortcuts import render
from random import randint
from unittest.mock import Mock

# Create your views here.

#def guess(request):
    # randint = Mock()
    # randint.return_value = 8
    #return render(request, 'guess/guess.html', {'random_number': randint(1,10)})

def guess(request):
    return render(request, 'guess/guess.html')