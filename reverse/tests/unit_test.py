from django.test import TestCase
from django.urls import resolve

from reverse.views import reverse

class ReverseAppTest(TestCase):

    def test_url_resolves_to_correct_view(self):
        view = resolve('/reverse/')
        assert view.func == reverse

    def test_uses_correct_template(self):
        response = self.client.get('/reverse/')
        self.assertTemplateUsed(response, 'reverse/reverse.html')

    def test_has_correct_title(self):
        response = self.client.get('/reverse/')
        assert 'reverse' in response.content.decode()

    def test_view_reverses_submitted_text(self):
        response = self.client.post('/reverse/', data={'item_to_reverse': 'frog'})
        assert 'gorf' in response.content.decode()
