from unittest.case import skip
from django.test import TestCase
from django.urls import resolve

from dice.views import *

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

class DiceAppStartTest(TestCase):

    def test_page_response_ok(self):
        assert self.client.get('/dice/start/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/dice/start/')
        assert view.func == start

    def test_uses_correct_template(self):
        response = self.client.get('/dice/start/')
        self.assertTemplateUsed(response, 'dice/start.html')

    def test_has_correct_title(self):
        response = self.client.get('/dice/start/')
        assert "<h2 id='header'>Dice</h2>" in response.content.decode()

    def test_has_rules_text(self):
        response = self.client.get('/dice/start/')
        assert "<p id='rules'>" in response.content.decode()

    def test_has_player_input(self):
        response = self.client.get('/dice/start/')
        assert "<input type='text' name='player' placeholder='enter player name'>" in response.content.decode()
    
    def test_has_play_button(self):
        response = self.client.get('/dice/start/')
        assert "<button type='submit'>Play</button>" in response.content.decode()


class DiceAppNewGameTest(TestCase):

    def test_form_action_correct_endpoint_from_start_page(self):
        response = self.client.get('/dice/start/')
        assert "<form action='/dice/game/' method='post'>" in response.content.decode()
    
    def test_page_response_ok(self):
        assert self.client.get('/dice/game/').status_code == 200

    def test_url_resolves_to_correct_view(self):
        view = resolve('/dice/game/')
        assert view.func == game

    def test_uses_correct_template(self):
        response = self.client.get('/dice/game/')
        self.assertTemplateUsed(response, 'dice/game.html')

    def test_player_name_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<p id='player'>Player: Questy</p>" in response.content.decode()

    def test_level_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<h2 id='header'>Level: 1</h2>" in response.content.decode()

    def test_rolls_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<p id='rolls'>Rolls: 2</p>" in response.content.decode()

    def test_score_to_beat_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<span id='score_to_beat'>2</span>" in response.content.decode()

    def test_score_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<p id='score'>Score: 0</p>" in response.content.decode()

    def test_roll_dice_button_on_page(self):
        response = self.client.get('/dice/game/')
        assert "<button type=submit>Roll Dice!</button>" in response.content.decode()