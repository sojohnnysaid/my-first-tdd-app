from unittest.case import skip
from django.test import TestCase
from django.urls import resolve

from dice.views import *

# http request -> url
# url rules decide which view function resolve the url
# view function returns an http response

# testing:
# can we resolve the url to a view?
# can we make the view return html?

