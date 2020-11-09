from django.urls import path

from guestbook.views import GuestListView, GuestCreateView

urlpatterns = [
    path('view/', GuestListView.as_view(), name='guestbook'),
    path('new/', GuestCreateView.as_view(success_url='/guestbook/view/'), name='new_guest'),
]
