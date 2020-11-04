from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

class DjangoSetupTest(FunctionalTest):
    # We've setup our project and can view the default Django welcome page
    def test_django_default_welcome_page(self):
        self.browser.get(f'{self.live_server_url}/default-welcome-page/')