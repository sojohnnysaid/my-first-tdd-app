from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys


class GuestbookAppTest(FunctionalTest):

    def test_user_can_sign_the_guestbook(self):

        # John wants to forever be remembered on the mini apps website
        # he goes to the guestbook page
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('guestbook').click()
        assert self.browser.current_url == f'{self.live_server_url}/guestbook/new/'

        # He notices the title says Sign our Guestbook
        header_text = self.browser.find_element_by_tag_name('h2').text
        assert 'Sign our Guestbook' == header_text

        # John sees an inputbox that says enter your full name
        inputbox = self.browser.find_element_by_name('name')

        # he fills in the inputbox with his full name
        inputbox.send_keys('John Smith')

        # He submites his name
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page reloads and shows a list of names
        assert self.browser.current_url == f'{self.live_server_url}/guestbook/view/'
        
        # He sees his name on the list
        list = self.browser.find_elements_by_tag_name('li')
        assert 'John Smith' in [item.text for item in list]