from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from guestbook.models import Guest
# Create your views here.

class GuestListView(ListView):
    model = Guest
    template_name = 'guestbook/guestbook.html'
    context_object_name = 'guestbook'

class GuestCreateView(CreateView):
    model = Guest
    template_name = 'guestbook/new_guest.html'
    fields = ['name']