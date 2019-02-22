from django.test import TestCase
from lists.views import home_page
from lists.models import Item
# from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')                 # Django Test Client
        self.assertTemplateUsed(response, 'home.html')  # will only work for response objects from Django Test Client

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'Tis a new item'})
        self.assertIn('Tis a new item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()
        second_item = Item()
        second_item.text = "Second Item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Second Item')