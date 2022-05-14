from urllib import request, response
from django.test import TestCase
from django.urls import reverse

class ThingTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("home")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_list_page_template(self):
        url = reverse("about")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")