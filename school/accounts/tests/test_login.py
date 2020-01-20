from django.test import TestCase
from django.shortcuts import reverse


class UnknownUserTest(TestCase):
    """
    Test for Unknown User Login
    """

    def test_redirects_to_login_page_for_unknown_user(self):
        url = "/"
        response = self.client.get(url, follow=True)
        self.assertRedirects(
            response,
            expected_url="{}?next={}".format(reverse("login"), url),
            target_status_code=200,
        )
        url = reverse("password_change")
        response = self.client.get(url, follow=True)
        self.assertRedirects(
            response,
            expected_url="{}?next={}".format(reverse("login"), url),
            target_status_code=200,
        )
        url = reverse("password_change_done")
        response = self.client.get(url, follow=True)
        self.assertRedirects(
            response,
            expected_url="{}?next={}".format(reverse("login"), url),
            target_status_code=200,
        )
        url = reverse("student_list")
        response = self.client.get(url, follow=True)
        self.assertRedirects(
            response,
            expected_url="{}?next={}".format(reverse("login"), url),
            target_status_code=200,
        )
        url = reverse("teacher_create")
        response = self.client.get(url, follow=True)
        self.assertRedirects(
            response,
            expected_url="{}?next={}".format(reverse("login"), url),
            target_status_code=200,
        )
