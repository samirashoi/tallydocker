from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_into_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)