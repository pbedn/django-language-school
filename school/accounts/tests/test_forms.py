import decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import datetime

from ..forms import CustomUserCreationForm, StudentCreationForm, TeacherCreationForm, StudentForm, TeacherForm


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
        user_form = form.save()
        self.assertEqual(user_form.email, "test@example.com")
        self.user = get_user_model().objects.get(email="test@example.com")
        self.assertEqual(self.user.check_password("SuperStrong123###"), True)

    def test_blank_data(self):
        CustomUserCreationForm({})
        # CustomUser cannot be created because for do not validate
        self.assertRaises(ValueError)


class StudentCreationFormTest(TestCase):
    """
    Tests for StudentCreation form
    """

    def test_student_is_created(self):
        form = StudentCreationForm(
            {
                "email": "test@example.com",
            }
        )
        self.assertTrue(form.is_valid())
        student_form = form.save()
        self.assertEqual(student_form.email, "test@example.com")
        self.user = get_user_model().objects.get(email="test@example.com")
        self.assertIsNotNone(self.user.password)
        self.assertTrue(self.user.is_student)
        self.assertFalse(self.user.is_teacher)


class TeacherCreationFormTest(TestCase):
    """
    Tests for TeacherCreation form
    """

    def test_teacher_is_created(self):
        form = TeacherCreationForm(
            {
                "email": "test@example.com",
            }
        )
        self.assertTrue(form.is_valid())
        teacher_form = form.save()
        self.assertEqual(teacher_form.email, "test@example.com")
        self.user = get_user_model().objects.get(email="test@example.com")
        self.assertIsNotNone(self.user.password)
        self.assertTrue(self.user.is_teacher)
        self.assertFalse(self.user.is_student)


class StudentFormTest(TestCase):
    """
    Tests for Student form
    """

    def test_student_form_is_valid(self):
        form = StudentForm(
            {
                "email": "test@example.com",
                "first_name": "Student",
                "last_name": "LastName",
                "phone": "",
                "general_discount": 0,
                "date_of_birth": datetime(2000, 1, 1),
                "company_name": "",
                "company_address": "",
                "company_tax_number": "",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['first_name'], "Student")
        self.assertEqual(form.cleaned_data['last_name'], "LastName")

    def test_student_form_is_invalid(self):
        form = StudentForm(
            {
                "email": "test@example.com",
                "first_name": "Student",
            }
        )
        self.assertFalse(form.is_valid())


class TeacherFormTest(TestCase):
    """
    Tests for Teacher form
    """

    def test_teacher_form_is_valid(self):
        form = TeacherForm(
            {
                "email": "test@example.com",
                "first_name": "Teacher",
                "last_name": "LastName",
                "phone": "12345",
                "notes": "",
                "date_of_birth": datetime(2000, 1, 1),
                "basic_course_rate": decimal.Decimal(0.0),
                "basic_individual_lesson_rate": decimal.Decimal(0.0),
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['first_name'], "Teacher")
        self.assertEqual(form.cleaned_data['last_name'], "LastName")
        self.assertEqual(form.cleaned_data['phone'], "12345")

    def test_teacher_form_is_invalid(self):
        form = TeacherForm(
            {
                "email": "test@example",
                "first_name": "Teacher",
                "last_name": "LastName",
            }
        )
        self.assertFalse(form.is_valid())
