from django.test import TestCase
from lists.views import home_page
# from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')                 # Django Test Client
        self.assertTemplateUsed(response, 'home.html')  # will only work for response objects from Django Test Client
