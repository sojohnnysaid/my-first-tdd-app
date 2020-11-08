from django.test import TestCase
from django.urls import resolve
from unittest.mock import patch

from guess import views


# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

# class GuessAppTest(TestCase):
    
#     @patch('guess.views.randint')
#     def test_mock(self, randint):
#         randint.return_value = 8
#         response = self.client.get('/guess/')
        
#         randint.assert_called_once_with(1,10)
#         assert "<p id='random-number'>8</p>" in response.content.decode()

class GuessAppTest(TestCase):

    def test_page_response_ok(self):
        assert self.client.get('/guess/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/guess/')
        assert view.func == views.guess

    def test_uses_correct_template(self):
        response = self.client.get('/guess/')
        self.assertTemplateUsed(response, 'guess/guess.html')

    def test_has_correct_header(self):
        response = self.client.get('/guess/')
        assert "<h2 id='header'>Guess the Number</h2>" in response.content.decode()

    def test_has_correct_content(self):
        response = self.client.get('/guess/')
        self.assertContains(response, 'Rules')

    