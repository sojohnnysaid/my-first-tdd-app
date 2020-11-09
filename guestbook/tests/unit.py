from django.test import TestCase
from django.urls import resolve

from guestbook import views

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

class GuestbookNewTest(TestCase):

    def test_page_response_ok(self):
        assert self.client.get('/guestbook/new/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/guestbook/new/')
        assert view.func.__name__ == views.GuestCreateView.as_view().__name__

    def test_uses_correct_template(self):
        response = self.client.get('/guestbook/new/')
        self.assertTemplateUsed(response, 'guestbook/new_guest.html')

    def test_has_correct_header(self):
        response = self.client.get('/guestbook/new/')
        self.assertContains(response, "<h2 id='header'>Sign our Guestbook</h2>")

    def test_form_submit_redirects_correctly(self):
        response = self.client.post('/guestbook/new/', {'name': 'John Smith'}, follow=True)
        self.assertContains(response, "<h2 id='header'>Guestbook</h2>")


class GuestbookViewTest(TestCase):
    def test_page_response_ok(self):
        assert self.client.get('/guestbook/view/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/guestbook/view/')
        assert view.func.__name__ == views.GuestCreateView.as_view().__name__

    def test_uses_correct_template(self):
        response = self.client.get('/guestbook/view/')
        self.assertTemplateUsed(response, 'guestbook/view_guest.html')

    def test_has_correct_header(self):
        response = self.client.get('/guestbook/view/')
        self.assertContains(
            response, "<h2 id='header'>Sign our Guestbook</h2>")
