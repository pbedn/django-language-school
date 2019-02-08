from django.test import TestCase
from django.shortcuts import reverse

from school.accounts.factories import StudentFactory, TeacherFactory, UserFactory
from school.accounts.models import Student, Teacher


class StudentListViewTest(TestCase):
    """
    Test for StudentList view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_can_display_student_list(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.first_name)

    def test_correct_template_is_used(self):
        self.client.get(reverse("student_list"))
        self.assertTemplateUsed("accounts/student_list.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(reverse("student_list"), "/accounts/student/")


class StudentCreateViewTest(TestCase):
    """
    Test for StudentCreate view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        self.client.get(reverse("student_create"))
        self.assertTemplateUsed("accounts/student_create.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(reverse("student_create"), "/accounts/student/create/")

    def test_get(self):
        response = self.client.get(reverse("student_create"))
        self.assertEqual(response.status_code, 200)

    def test_post_when_form_is_valid(self):
        student_count = Student.objects.count()
        self.assertEqual(student_count, 1)
        url = reverse("student_create")
        data = {
            "email": "first@example.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "phone": "",
            "general_discount": "",
            "date_of_birth": "",
            "company_name": "",
            "company_address": "",
            "company_tax_number": "",
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["student"].user.email, data["email"])
        self.assertEqual(
            response.context_data["student"].first_name, data["first_name"]
        )
        self.assertEqual(response.context_data["student"].last_name, data["last_name"])
        student_count = Student.objects.count()
        self.assertEqual(student_count, 2)

    def test_post_when_form_is_invalid(self):
        student_count = Student.objects.count()
        self.assertEqual(student_count, 1)
        url = reverse("student_create")
        data = {"email": "test@example.com", "first_name": "Student"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(student_count, 1)


class StudentDetailViewTest(TestCase):
    """
    Test for StudentDetail view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_can_display_student_detail(self):
        url = reverse("student_detail", args=[self.student.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.first_name)

    def test_correct_template_is_used(self):
        url = reverse("student_detail", args=[self.student.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/student_detail.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("student_detail", args=[self.student.pk])
        self.assertEqual(url, "/accounts/student/detail/{}/".format(self.student.pk))


class StudentUpdateViewTest(TestCase):
    """
    Test for StudentUpdate view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        url = reverse("student_update", args=[self.student.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/student_update.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("student_update", args=[self.student.pk])
        self.assertEqual(url, "/accounts/student/update/{}/".format(self.student.pk))

    def test_get(self):
        url = reverse("student_update", args=[self.student.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=self.student.user.email)
        self.assertContains(response, text=self.student.first_name)
        self.assertContains(response, text=self.student.last_name)

    def test_post_with_form_valid(self):
        """Test that Student object has been updated"""
        url = reverse("student_update", args=[self.student.pk])
        data = {
            "email": "second@example.com",
            "first_name": "FirstNameUpdated",
            "last_name": "LastNameUpdated",
            "phone": "",
            "general_discount": "",
            "date_of_birth": "",
            "company_name": "",
            "company_address": "",
            "company_tax_number": "",
        }
        response = self.client.post(url, data=data, follow=True)
        student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("student_list"))
        self.assertContains(response, text=data["email"])
        self.assertContains(response, text=data["first_name"])
        self.assertContains(response, text=data["last_name"])
        self.assertEqual(student.user.email, data["email"])
        self.assertEqual(student.first_name, data["first_name"])
        self.assertEqual(student.last_name, data["last_name"])

    def test_post_with_form_invalid(self):
        """Test if Student object was not changed and return error on email field"""
        url = reverse("student_update", args=[self.student.pk])
        data = {
            "email": "second",
            "first_name": "FirstNameUpdated",
            "last_name": "LastNameUpdated",
        }
        response = self.client.post(url, data=data, follow=True)
        student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Enter a valid email address.")
        self.assertEqual(self.student.user.email, student.user.email)
        self.assertEqual(self.student.first_name, student.first_name)
        self.assertEqual(self.student.last_name, student.last_name)


class StudentDeleteViewTest(TestCase):
    """
    Test for StudentDelete view
    """

    def setUp(self):
        self.student = StudentFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        url = reverse("student_delete", args=[self.student.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/student_delete.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("student_delete", args=[self.student.pk])
        self.assertEqual(url, "/accounts/student/delete/{}/".format(self.student.pk))

    def test_url_redirects_correctly(self):
        url = reverse("student_delete", args=[self.student.pk])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse("student_list"))

    def test_student_has_been_deleted(self):
        student_count = Student.objects.count()
        self.assertEqual(student_count, 1)
        url = reverse("student_delete", args=[self.student.pk])
        response = self.client.post(url)
        student_count = Student.objects.count()
        self.assertEqual(student_count, 0)


class TeacherListViewTest(TestCase):
    """
    Test for TeacherList view
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_can_display_teacher_list(self):
        response = self.client.get(reverse("teacher_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.teacher.first_name)

    def test_correct_template_is_used(self):
        self.client.get(reverse("teacher_list"))
        self.assertTemplateUsed("accounts/teacher_list.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(reverse("teacher_list"), "/accounts/teacher/")


class TeacherCreateViewTest(TestCase):
    """
    Test for TeacherCreate view
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        self.client.get(reverse("teacher_create"))
        self.assertTemplateUsed("accounts/teacher_create.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(reverse("teacher_create"), "/accounts/teacher/create/")

    def test_get(self):
        response = self.client.get(reverse("teacher_create"))
        self.assertEqual(response.status_code, 200)

    def test_post_when_form_is_valid(self):
        teacher_count = Teacher.objects.count()
        self.assertEqual(teacher_count, 1)
        url = reverse("teacher_create")
        data = {
            "email": "test@example.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "phone": "12345",
            "notes": "",
            "date_of_birth": "",
            "basic_course_rate": "",
            "basic_individual_lesson_rate": "",
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["teacher"].user.email, data["email"])
        self.assertEqual(
            response.context_data["teacher"].first_name, data["first_name"]
        )
        self.assertEqual(response.context_data["teacher"].last_name, data["last_name"])
        teacher_count = Teacher.objects.count()
        self.assertEqual(teacher_count, 2)

    def test_post_when_form_is_invalid(self):
        teacher_count = Teacher.objects.count()
        self.assertEqual(teacher_count, 1)
        url = reverse("teacher_create")
        data = {
            "email": "test@example.com",
            "first_name": "FirstName",
            "last_name": "LastName",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(teacher_count, 1)


class TeacherDetailViewTest(TestCase):
    """
    Test for TeacherDetail view
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_can_display_teacher_detail(self):
        url = reverse("teacher_detail", args=[self.teacher.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.teacher.first_name)

    def test_correct_template_is_used(self):
        url = reverse("teacher_detail", args=[self.teacher.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/teacher_detail.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("teacher_detail", args=[self.teacher.pk])
        self.assertEqual(url, "/accounts/teacher/detail/{}/".format(self.teacher.pk))


class TeacherUpdateViewTest(TestCase):
    """
    Test for TeacherUpdate view
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        url = reverse("teacher_update", args=[self.teacher.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/teacher_update.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("teacher_update", args=[self.teacher.pk])
        self.assertEqual(url, "/accounts/teacher/update/{}/".format(self.teacher.pk))

    def test_get(self):
        url = reverse("teacher_update", args=[self.teacher.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=self.teacher.user.email)
        self.assertContains(response, text=self.teacher.first_name)
        self.assertContains(response, text=self.teacher.last_name)

    def test_post_with_form_valid(self):
        """Test that Teacher object has been updated"""
        url = reverse("teacher_update", args=[self.teacher.pk])
        data = {
            "email": "second@example.com",
            "first_name": "FirstNameUpdated",
            "last_name": "LastNameUpdated",
            "phone": "123450000",
            "notes": "",
            "date_of_birth": "",
            "basic_course_rate": "",
            "basic_individual_lesson_rate": "",
        }
        response = self.client.post(url, data=data, follow=True)
        teacher = Teacher.objects.get(pk=self.teacher.pk)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("teacher_list"))
        self.assertContains(response, text=data["email"])
        self.assertContains(response, text=data["first_name"])
        self.assertContains(response, text=data["last_name"])
        self.assertContains(response, text=data["phone"])
        self.assertEqual(teacher.user.email, data["email"])
        self.assertEqual(teacher.first_name, data["first_name"])
        self.assertEqual(teacher.last_name, data["last_name"])
        self.assertEqual(teacher.phone, data["phone"])

    def test_post_with_form_invalid(self):
        """Test if Teacher object was not changed and return error on email field"""
        url = reverse("teacher_update", args=[self.teacher.pk])
        data = {
            "email": "second",
            "first_name": "FirstNameUpdated",
            "last_name": "LastNameUpdated",
            "phone": "123450000",
        }
        response = self.client.post(url, data=data, follow=True)
        teacher = Teacher.objects.get(pk=self.teacher.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Enter a valid email address.")
        self.assertEqual(self.teacher.user.email, teacher.user.email)
        self.assertEqual(self.teacher.first_name, teacher.first_name)
        self.assertEqual(self.teacher.last_name, teacher.last_name)
        self.assertEqual(self.teacher.phone, teacher.phone)


class TeacherDeleteViewTest(TestCase):
    """
    Test for TeacherDelete view
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_correct_template_is_used(self):
        url = reverse("teacher_delete", args=[self.teacher.pk])
        response = self.client.get(url)
        self.assertTemplateUsed("accounts/teacher_delete.html")

    def test_url_has_correct_reverse_url(self):
        url = reverse("teacher_delete", args=[self.teacher.pk])
        self.assertEqual(url, "/accounts/teacher/delete/{}/".format(self.teacher.pk))

    def test_url_redirects_correctly(self):
        url = reverse("teacher_delete", args=[self.teacher.pk])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse("teacher_list"))

    def test_teacher_has_been_deleted(self):
        teacher_count = Teacher.objects.count()
        self.assertEqual(teacher_count, 1)
        url = reverse("teacher_delete", args=[self.teacher.pk])
        response = self.client.post(url)
        teacher_count = Student.objects.count()
        self.assertEqual(teacher_count, 0)
