from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):
    
    def setUp(self):
        opts = Options()
        opts.add_argument('--headless')
        self.browser = webdriver.Chrome(options=opts)
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()