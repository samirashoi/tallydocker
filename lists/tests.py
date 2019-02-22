from django.test import TestCase
from lists.views import home_page
# from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')                 # Django Test Client
        self.assertTemplateUsed(response, 'home.html')  # will only work for response objects from Django Test Client

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'Tis a new item'})
        self.assertIn('Tis a new item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
