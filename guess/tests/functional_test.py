from unittest.case import skip
from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest.mock import patch

'''
guess           a number guessing game
------------------------------
how to win:     player's guess has to match the generated number
actors:         player
inputs:         player_guess, generated_number
outputs:        result
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
        # and fills in the inputbox that says enter guess
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

    @patch('guess.views.randint')
    def test_any_user_wins_round_of_guess(self, randint):

        ##------------------
        ## John's story
        ##------------------
        # John is on the guess app page
        self.browser.get(f'{self.live_server_url}/guess/')

        # Filled with determination, John guesses the number 8
        # and filles in the inputbox that says enter guess
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('8')


        ## we're replacing the random value with 8 so John has to win
        randint.return_value = 8
        # He submites his guess
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When the page reloads he sees the random numer is 8
        generated_number = self.browser.find_element_by_id('generated_number').text
        assert generated_number == '8'

        # The page also shows the number he guessed
        player_guess = self.browser.find_element_by_id('player_guess').text
        assert player_guess == '8'
        
        # There is a message that tells him he guessed correctly
        result = self.browser.find_element_by_id('result').text
        self.assertRegex(result,r'correctly')


        ##------------------
        ## Janes's story
        ##------------------
        # Jane is on the guess app page
        self.browser.get(f'{self.live_server_url}/guess/')

        # Filled with determination, Jane guesses the number 7
        # and filles in the inputbox that says enter guess
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('7')

        # She submites his guess
        ## we're replacing the random value with 7 so Jane has to win
        randint.return_value = 7
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When the page reloads She sees the random numer is 7
        generated_number = self.browser.find_element_by_id('generated_number').text
        assert generated_number == '7'

        # The page also shows the number she guessed
        player_guess = self.browser.find_element_by_id('player_guess').text
        assert player_guess == '7'
        
        # There is a message that tells her she guessed correctly
        result = self.browser.find_element_by_id('result').text
        self.assertRegex(result,r'correctly')


    @patch('guess.views.randint')
    def test_any_user_loses_round_of_guess(self, randint):

        ##------------------
        ## John's story
        ##------------------
        # John is on the guess app page
        self.browser.get(f'{self.live_server_url}/guess/')

        # Filled with determination, John guesses the number 8
        # and filles in the inputbox that says enter guess
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('8')


        ## we're replacing the random value with 8 so John has to lose
        randint.return_value = 2
        # He submites his guess
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When the page reloads he sees the random numer is 2
        generated_number = self.browser.find_element_by_id('generated_number').text
        assert generated_number == '2'

        # The page also shows the number he guessed
        player_guess = self.browser.find_element_by_id('player_guess').text
        assert player_guess == '8'
        
        # There is a message that tells him he guessed incorrectly
        result = self.browser.find_element_by_id('result').text
        self.assertRegex(result,r'incorrectly')


        ##------------------
        ## Janes's story
        ##------------------
        # Jane is on the guess app page
        self.browser.get(f'{self.live_server_url}/guess/')

        # Filled with determination, Jane guesses the number 7
        # and filles in the inputbox that says enter guess
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('7')

        # She submites his guess
        ## we're replacing the random value with 2 so Jane has to lose
        randint.return_value = 2
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When the page reloads She sees the random numer is 2
        generated_number = self.browser.find_element_by_id('generated_number').text
        assert generated_number == '2'

        # The page also shows the number she guessed
        player_guess = self.browser.find_element_by_id('player_guess').text
        assert player_guess == '7'
        
        # There is a message that tells her she guessed incorrectly
        result = self.browser.find_element_by_id('result').text
        self.assertRegex(result,r'incorrectly')

    
    def test_user_inputs_invalid_guess(self):

        # Ron wants to burn it all down
        # he decides to enter sdlfja;lkj into the inputbox
        self.browser.get(f'{self.live_server_url}/guess/')
        inputbox = self.browser.find_element_by_name('player_guess')
        inputbox.send_keys('sdlfja;lkj')

        # He submits his garbage input
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # But quickly realizes the system will only accept valid data
        error_message = self.browser.find_elements_by_class_name('error')[0].text
        assert 'please enter a value from 1 to 10' in error_message