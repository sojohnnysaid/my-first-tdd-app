from django.test import TestCase

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

class GuessAppTest(TestCase):
    
    def test_pass(self):
        pass