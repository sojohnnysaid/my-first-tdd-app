from tests.base_functional_test import FunctionalTest


class HomePageTest(FunctionalTest):
    def test_can_visit_homepage_to_view_app_links(self):
        # John wants to try some apps on our website so he goes to the homepage
        self.browser.get(self.live_server_url)

        # He notices the title and header
        assert self.browser.title == self.PROJECT_TITLE
        header_text = self.browser.find_element_by_tag_name('h1').text
        assert header_text == self.PROJECT_TITLE

        # John likes the design of the homepage with the app list centered
        self.browser.set_window_size(1024, 768)
        list = self.browser.find_element_by_id('app-list')
        self.assertAlmostEqual(
            list.location['x'] + (list.size['width'] / 2),
            512,
            delta=10
        )

        # The app list items are links
        app_list = self.browser.find_elements_by_tag_name('li')
        assert len(app_list) > 0
        list_item = self.browser.find_element_by_link_text('reverse')
        assert list_item.get_attribute('href') == f'{self.live_server_url}/reverse/'

        # John clicks the reverse link and it brings him to the reverse app
        self.browser.find_element_by_link_text('reverse').click()