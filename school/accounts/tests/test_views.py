from django.test import Client, TestCase
from django.contrib.auth import get_user_model

from ..views import SignUpCreateView


class SignUpCreateViewTestCase(TestCase):
    """
    Test for SignUp view
    """
    def setUp(self):
        self.client = Client()

    def test_correct_template_is_used(self):
        r = self.client.get('')
        self.assertTemplateUsed('registration/login.html')

    def test_reverse_success_url(self):
        self.assertEqual(SignUpCreateView.success_url, '/accounts/login/')
