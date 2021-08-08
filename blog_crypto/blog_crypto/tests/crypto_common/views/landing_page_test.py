from django.test import TestCase, Client
from django.urls import reverse


class LandingPageTest(TestCase):
    def test_return_landing_page(self):
        client = Client()
        response = client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page.html')
