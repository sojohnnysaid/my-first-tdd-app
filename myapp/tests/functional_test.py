from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys

class HomePageTest(FunctionalTest):
    def test_can_visit_homepage_to_view_app_links(self):
        # John wants to try some apps on our website so he goes to the homepage
        self.browser.get(self.live_server_url)

        # He notices the title and header say "mini apps"
        assert self.browser.title == "mini apps"
        header_text = self.browser.find_element_by_tag_name('h1').text
        assert header_text == "mini apps"

        # the first app is called "string reverse"
        string_reverse_title = self.browser.find_element_by_id('string-reverse-title').text
        assert string_reverse_title == "string reverse"

        # the inputbox invites him to type in a word
        inputbox = self.browser.find_element_by_id('string-reverse-input')
        assert inputbox.get_attribute('placeholder') == 'Enter a word'

        # John decides to type in the word frog
        inputbox.send_keys('frog')

        # when he hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # and now the page shows the word frog backwards
        string_reverse_result = self.browser.find_element_by_id('string-reverse-result').text
        assert string_reverse_result == 'gorf'

        # happy with the results he moves on to the next mini app
        self.fail('write more tests!')