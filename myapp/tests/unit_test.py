from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import resolve
from myapp import views


from myapp.views import home_page

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response


# testing:
# can we resolve the url to a view?
# can we make the view return html?

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        view = resolve('/')
        assert view.func == home_page

    def test_home_page_uses_correct_template(self):
        response = self.client.get('')
        assert response.content.decode() == render_to_string('home.html')

    def test_home_page_has_correct_title(self):
        response = self.client.get('')
        assert 'mini apps' in response.content.decode()