from selenium.webdriver.support.wait import time
from tests.base_functional_test import FunctionalTest
from selenium.webdriver.common.keys import Keys


class StringReverseAppTest(FunctionalTest):
    def test_can_visit_string_reverse_to_view_app_links(self):
        # John goes to check out the reverse mini app
        self.browser.get(f'{self.live_server_url}/reverse')

        # He notices the header says "Reverse"
        header_text = self.browser.find_element_by_tag_name('h2').text
        assert header_text == "Reverse"

        # the inputbox invites him to type in a word
        inputbox = self.browser.find_element_by_id('string-reverse-input')
        assert inputbox.get_attribute('placeholder') == 'Enter a word'

        # John decides to type in the word frog
        inputbox.send_keys('frog')

        # when he hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # and now the page shows the word frog backwards
        string_reverse_result = self.browser.find_element_by_id(
            'string-reverse-result').text
        assert string_reverse_result == 'gorf'

        # happy with the results he goes back to the homepage
        self.browser.find_element_by_link_text(self.PROJECT_TITLE).click()
