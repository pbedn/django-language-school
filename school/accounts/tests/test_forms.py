import decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import datetime

from ..forms import (
    CustomUserCreationForm,
    StudentCreationForm,
    TeacherCreationForm,
    StudentForm,
    TeacherForm,
)


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
        form = StudentCreationForm({"email": "test@example.com"})
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
        form = TeacherCreationForm({"email": "test@example.com"})
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

    def setUp(self):
        self.correct_form = {
            "email": "test@example.com",
            "first_name": "Student",
            "last_name": "LastName",
            "phone": "123456789",
            "general_discount": 0,
            "date_of_birth": datetime(2000, 1, 1),
            "company_name": "",
            "company_address": "",
            "company_tax_number": "123-456789-5",
        }

    def test_student_form_is_valid(self):
        form = StudentForm(self.correct_form)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["first_name"], "Student")
        self.assertEqual(form.cleaned_data["last_name"], "LastName")
        self.assertEqual(form.cleaned_data["phone"], "123456789")

    def test_student_form_is_invalid(self):
        form = StudentForm({"email": "test@example.com", "first_name": "Student"})
        self.assertFalse(form.is_valid())

    def test_phone_number_has_correct_length(self):
        form = StudentForm(self.correct_form)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.cleaned_data["phone"]), 9)

    def test_company_tax_number_is_numeric_and_has_correct_length(self):
        """
        Ensure correct NIP number in format
            123 456789 5
            123-456789-5
            1234567890
            ..
        """
        form = StudentForm(self.correct_form)
        self.assertTrue(form.is_valid())
        self.assertTrue(
            all(
                map(
                    lambda x: x.isdigit(),
                    form.cleaned_data["company_tax_number"].split("-"),
                )
            )
        )
        self.assertTrue(len(form.cleaned_data["company_tax_number"]) > 10)


class TeacherFormTest(TestCase):
    """
    Tests for Teacher form
    """

    def setUp(self):
        self.correct_form = {
            "email": "test@example.com",
            "first_name": "Teacher",
            "last_name": "LastName",
            "phone": "123456789",
            "notes": "",
            "date_of_birth": datetime(2000, 1, 1),
            "basic_course_rate": decimal.Decimal(0.0),
            "basic_individual_lesson_rate": decimal.Decimal(0.0),
        }

    def test_teacher_form_is_valid(self):
        form = TeacherForm(self.correct_form)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["first_name"], "Teacher")
        self.assertEqual(form.cleaned_data["last_name"], "LastName")
        self.assertEqual(form.cleaned_data["phone"], "123456789")

    def test_teacher_form_is_invalid(self):
        form = TeacherForm(
            {"email": "test@example", "first_name": "Teacher", "last_name": "LastName"}
        )
        self.assertFalse(form.is_valid())

    def test_phone_number_has_correct_length(self):
        form = TeacherForm(self.correct_form)
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.cleaned_data["phone"]), 9)
