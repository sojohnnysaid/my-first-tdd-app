from django.test import TestCase
from django.urls import resolve

from guestbook import views

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

class GuestbookAppTest(TestCase):

    def test_page_response_ok(self):
        assert self.client.get('/guestbook/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/guestbook/')
        assert view.func == views.guestbook

    def test_uses_correct_template(self):
        response = self.client.get('/guestbook/')
        self.assertTemplateUsed(response, 'guestbook/guestbook.html')

    def test_has_correct_header(self):
        response = self.client.get('/guestbook/')
        assert "<h2 id='header'>Guestbook</h2>" in response.content.decode()