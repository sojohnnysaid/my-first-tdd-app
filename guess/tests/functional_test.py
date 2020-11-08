from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys

'''
guess               a number guessing game
------------------------------
how to win:     player's guess has to match the generated number
actors:         player
inputs:         player_guess, generated_number
scenarios:      player wins, player loses
'''


class GuessAppTest(FunctionalTest):
    
    def test_user_plays_round_of_guess(self):
        # John starts on the homepage and decides to try the guess app
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('guess').click()
        assert self.browser.current_url == f'{self.live_server_url}/guess/'

        # He notices the title says Guess the Number
        header_text = self.browser.find_element_by_tag_name('h2').text
        assert 'Guess the Number' == header_text

        # John reads the game rules on the page
        rules_text = self.browser.find_element_by_id('rules').text
        assert 'Rules' in rules_text

        # Filled with determination, John guesses the number 8
        # and filles in the inputbox that says enter guess
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('8')

        # He submites his guess
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When the page reloads he sees a message
        # The message tells him the result of his guess
        result = self.browser.find_element_by_id('result').text
        self.assertRegex(result,r'correctly|incorrectly')

        # He sees a link that says play again and clicks it
        # It brings him back to the Guess the number page
        self.browser.find_element_by_link_text('play again').click()
        assert self.browser.current_url == f'{self.live_server_url}/guess/'