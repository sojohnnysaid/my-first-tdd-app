from django.test import TestCase

class ReverseAppTest(TestCase):

    def test_view_reverses_submitted_text(self):
        response = self.client.post('/reverse/', data={'item_to_reverse': 'frog'})
        assert 'gorf' in response.content.decode()
