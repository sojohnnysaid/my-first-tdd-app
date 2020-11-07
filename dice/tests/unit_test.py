from django.test import TestCase
from django.urls import resolve

from dice.views import dice

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

class DiceAppTest(TestCase):
    def test_page_response_ok(self):
        assert self.client.get('/dice/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/dice/')
        assert view.func == dice

    def test_uses_correct_template(self):
        response = self.client.get('/dice/')
        self.assertTemplateUsed(response, 'dice/dice.html')

    def test_has_correct_title(self):
        response = self.client.get('/dice/')
        assert "<h2 id='app-title'>Dice</h2>" in response.content.decode()

    def test_has_rules_text(self):
        response = self.client.get('/dice/')
        assert "<p id='rules'>" in response.content.decode()

    def test_has_player_input(self):
        response = self.client.get('/dice/')
        assert "<input type='text' name='player' placeholder='enter player name'>" in response.content.decode()
    
    def test_has_play_button(self):
        response = self.client.get('/dice/')
        assert "<button type='submit'>Play</button>" in response.content.decode()