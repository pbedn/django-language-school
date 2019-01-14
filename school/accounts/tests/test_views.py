from django.test import Client, TestCase
from django.shortcuts import reverse


class StudentListViewTest(TestCase):
    """
    Test for StudentListView
    """
    def setUp(self):
        self.client = Client()

    def test_correct_model_is_used(self):
        res = self.client.get('student')
        self.fail()

    def test_correct_template_is_used(self):
        self.client.get('')
        self.assertTemplateUsed('accounts/student_list.html')

    def test_correct_url_has_correct_reverse_url(self):
        self.assertEqual(reverse('student_list'), '/accounts/student/')

