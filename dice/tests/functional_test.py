from unittest.case import skip
from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys


class DiceAppTest(FunctionalTest):

    
    def test_can_visit_dice_start_page(self):
        # John wants to play the dice game
        # so he goes to the dice page from the homepage
        self.browser.get(f'{self.live_server_url}')
        self.browser.find_element_by_link_text('dice').click()
        self.browser.get(f'{self.live_server_url}/dice')

        # He notices the header says "Dice"
        header_text = self.browser.find_element_by_tag_name('h2').text
        assert header_text == 'Dice'

        # There is some text explaining the rules
        rules = self.browser.find_element_by_id('rules').text
        self.assertRegex(rules,'.+')

        # There is an inputbox that says 'enter player name'
        inputbox = self.browser.find_element_by_name('player')
        assert inputbox.get_attribute('placeholder') == 'enter player name'

        # John enters his player name 'Questy'
        inputbox.send_keys('Questy')

        # underneath the input box is a button that says play
        button = self.browser.find_element_by_tag_name('button')
        assert button.text == 'Play'

        # he clicks the button and is taken to a new page
        button.click()

    @skip
    def test_can_start_new_dice_game(self):
        # the url now points to /game
        self.browser.get(f'{self.live_server_url}/dice/game')

        # the page now shows:
        # player name: Questy
        # level: 1
        # rolls left: 2
        # score to beat: (a random number from 2-24)
        # total score: 0

    @skip
    def test_can_start_dice_game_from_last_visit(self):
        # the url now points to /game
        self.browser.get(f'{self.live_server_url}/dice/game')

        # John has played the first level already
        # the page now shows:
        # player name: Questy
        # level: 2
        # rolls left: 2
        # score to beat: (a random number from 2-24)
        # total score: 0

    @skip
    def player_wins_dice_match(self):
        pass
        # the page now shows:
        # player name: Questy
        # level: 1
        # rolls left: 2
        # score to beat: 2
        # total score: 0

        # John sees the button to roll the dice

        # He clicks the button

        # the page now updates:
        # rolls left: 1
        # total score: 6

        # on his final roll John is taken to a new url /result
        
        # the page shows the following game results:
        # result: player won
        # total score: 10
        # score to beat: 2

        # finally John notices a link that reads 'go to next level'

    @skip
    def player_loses_dice_match(self):
        pass
        # the page now shows:
        # player name: Questy
        # level: 1
        # rolls left: 2
        # score to beat: 12
        # total score: 0

        # John sees the button to roll the dice

        # He clicks the button

        # the page now updates:
        # rolls left: 1
        # total score: 2

        # on his final roll John is taken to a new url /result
        
        # the page shows the following game results:
        # result: player lost
        # total score: 4
        # score to beat: 12

        # finally John notices a link that reads 'try again'


