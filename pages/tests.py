from django.test import SimpleTestCase

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)

class AboutpagesTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)
    