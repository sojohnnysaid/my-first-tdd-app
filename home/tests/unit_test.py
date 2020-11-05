from unittest.case import skip
from django.test import TestCase
from django.urls import resolve

from home.views import home

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        view = resolve('/')
        assert view.func == home

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_page_has_correct_title(self):
        response = self.client.get('')
        assert 'mini apps' in response.content.decode()
