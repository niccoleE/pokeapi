from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm


class RegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse('users:register')
        self.short_password = {
            'username': 'useruser',
            'password1': '1_2',
            'password2': '1_2',
        }
        self.too_common = {
            'username': 'useruser',
            'password1': '11',
            'password2': '11',
        }
        self.user_ok = {
            'username': 'useruser',
            'password1': '11_2User',
            'password2': '11_2User',
        }

    def test_register_page_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_ok_redirect(self):
        """check if after succeessful registration redirects to index"""
        response = self.client.post(self.register_url, self.user_ok, format='text/html')
        self.assertRedirects(response, '/')

    def test_register_short_password(self):
        form = UserCreationForm(data=self.short_password)
        self.assertFalse(form.is_valid())

    def test_register_too_common_password(self):
        form = UserCreationForm(data=self.too_common)
        self.assertFalse(form.is_valid())

    def test_register_user_ok(self):
        form = UserCreationForm(data=self.user_ok)
        self.assertTrue(form.is_valid())



