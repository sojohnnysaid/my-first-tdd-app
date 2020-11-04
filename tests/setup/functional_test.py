from ..base_functional_test import FunctionalTest

class DjangoSetupTest(FunctionalTest):
    # We've setup our project and can view the default Django welcome page
    def test_django_default_welcome_page(self):
        self.browser.get(f'{self.live_server_url}/default-welcome-page/')
        assert 'Django' in self.browser.title