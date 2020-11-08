from django.shortcuts import render, redirect
from django.contrib import messages
from random import randint


# Create your views here.

#def guess(request):
    # randint = Mock()
    # randint.return_value = 8
    #return render(request, 'guess/guess.html', {'random_number': randint(1,10)})

def guess(request):
    if request.method == 'POST':
        player_guess = request.POST.get('player_guess')
        if(player_guess.isdigit() and int(player_guess) in range(1,10)):
            generated_number = str(randint(1,10))
            return render(
                request, 
                'guess/guess.html', 
                {
                    'player_guess': player_guess,
                    'generated_number': generated_number
                }
            )
        else:
            messages.error(request,'please enter a value from 1 to 10', extra_tags='list-group-item-danger')
            return redirect('/guess/')
    else:
        return render(request, 'guess/guess.html')