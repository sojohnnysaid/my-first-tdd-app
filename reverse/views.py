from django.shortcuts import render


def reverse(request):
    submitted_word = request.POST.get('item_to_reverse', '')
    reversed_word = submitted_word[::-1]
    return render(request, 'reverse/reverse.html', {'reversed_word': reversed_word})
