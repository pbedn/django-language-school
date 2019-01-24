from django.test import TestCase
from django.contrib.auth import get_user_model

from ..forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):
    """
    Tests for CustomUser form
    """

    def test_valid_data(self):
        form = CustomUserCreationForm(
            {
                "email": "test@example.com",
                "password1": "SuperStrong123###",
                "password2": "SuperStrong123###",
            }
        )
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.email, "test@example.com")
        self.user = get_user_model().objects.get(email="test@example.com")
        self.assertEqual(self.user.check_password("SuperStrong123###"), True)

    def test_blank_data(self):
        CustomUserCreationForm({})
        # CustomUser cannot be created because for do not validate
        self.assertRaises(ValueError)
