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

    def test_has_rules(self):
        response = self.client.get('/guess/')
        self.assertContains(response, 'Rules')

    def test_post_has_result_general_content(self):
        response = self.client.post('/guess/', {'player_guess': '3'})
        self.assertContains(response, 'Generated Number')
        self.assertContains(response, 'Your Guess')

    def test_post_has_player_guess(self):
        response = self.client.post('/guess/',{'player_guess': '3'})
        self.assertContains(response, "<span id='player_guess'>3")

    @patch('guess.views.randint')
    def test_random_number_called_once_with_correct_args(self, randint):
        response = self.client.post('/guess/', {'player_guess': '3'})
        randint.assert_called_once_with(1,10)

    @patch('guess.views.randint')
    def test_generated_number_is_a_string(self, randint):
        randint.return_value = 1
        response = self.client.post('/guess/',{'player_guess': '1'})
        self.assertEqual(response.context['generated_number'], '1')

    def test_error_message_generated_when_input_invalid(self):
        response = self.client.post('/guess/',{'player_guess': 'fja;'}, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "list-group-item-danger error")

    def test_error_message_shown_in_template(self):
        response = self.client.post('/guess/',{'player_guess': 'fja;'}, follow=True)
        self.assertContains(response, "please enter a value from 1 to 10")

    # to do test for all possible inputs from user