from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    """
    Tests for the CustomUser model
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user("test@example.com")

    def test_user_is_created(self):
        user = get_user_model().objects.all()[0]
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, getattr(self.user, "password"))


class StudentModelTest(TestCase):
    """
    Tests for the Student model
    """

    def setUp(self):
        pass
