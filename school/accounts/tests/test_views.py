from django.test import TestCase
from django.shortcuts import reverse

from school.accounts.factories import StudentFactory, TeacherFactory


class StudentListViewTest(TestCase):
    """
    Test for StudentListView
    """

    def setUp(self):
        self.student = StudentFactory()
        self.client.force_login(self.student.user)

    def test_can_login_and_display_student_list(self):
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
    Test for StudentCreateView
    """

    def setUp(self):
        self.student = StudentFactory()
        self.client.force_login(self.student.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_create_student(self):
        url = reverse("student_create")
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "phone",
            "general_discount": "general_discount",
            "date_of_birth": "date_of_birth",
            "company_name": "company_name",
            "company_address": "company_address",
            "company_tax_number": "company_tax_number",
            "user": self.student.user.pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)


class StudentDetailViewTest(TestCase):
    """
    Test for StudentDetailView
    """

    def setUp(self):
        self.student = StudentFactory()
        self.client.force_login(self.student.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_detail_student(self):
        url = reverse("student_detail", args=[self.student.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class StudentUpdateViewTest(TestCase):
    """
    Test for StudentUpdateView
    """

    def setUp(self):
        self.student = StudentFactory()
        self.client.force_login(self.student.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_update_student(self):
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "phone",
            "general_discount": "general_discount",
            "date_of_birth": "date_of_birth",
            "company_name": "company_name",
            "company_address": "company_address",
            "company_tax_number": "company_tax_number",
            "user": self.student.user.pk,
        }
        url = reverse("student_update", args=[self.student.pk])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class StudentDeleteViewTest(TestCase):
    """
    Test for StudentDeleteView
    """

    def setUp(self):
        self.student = StudentFactory()
        self.client.force_login(self.student.user)

    def test_correct_template_is_used(self):
        self.client.login(
            email=self.student.user.email, password=self.student.user.password
        )
        self.client.get(reverse("student_delete", args=[self.student.pk]), follow=True)
        self.assertTemplateUsed("accounts/student_delete.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(
            reverse("student_delete", args=[self.student.pk]),
            "/accounts/student/delete/{}/".format(self.student.pk),
        )


class TeacherListViewTest(TestCase):
    """
    Test for TeacherListView
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.client.force_login(self.teacher.user)

    def test_can_login_and_display_student_list(self):
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
    Test for TeacherCreateView
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.client.force_login(self.teacher.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_create_student(self):
        url = reverse("teacher_create")
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "phone",
            "notes": "notes",
            "date_of_birth": "date_of_birth",
            "basic_course_rate": "basic_course_rate",
            "basic_individual_lesson_rate": "basic_individual_lesson_rate",
            "user": self.teacher.user.pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)


class TeacherDetailViewTest(TestCase):
    """
    Test for TeacherDetailView
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.client.force_login(self.teacher.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_detail_student(self):
        url = reverse("teacher_detail", args=[self.teacher.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TeacherUpdateViewTest(TestCase):
    """
    Test for TeacherUpdateView
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.client.force_login(self.teacher.user)

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_update_teacher(self):
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "phone",
            "notes": "notes",
            "date_of_birth": "date_of_birth",
            "basic_course_rate": "basic_course_rate",
            "basic_individual_lesson_rate": "basic_individual_lesson_rate",
            "user": self.teacher.user.pk,
        }
        url = reverse("teacher_update", args=[self.teacher.pk])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class TeacherDeleteViewTest(TestCase):
    """
    Test for TeacherDeleteView
    """

    def setUp(self):
        self.teacher = TeacherFactory()
        self.client.force_login(self.teacher.user)

    def test_correct_template_is_used(self):
        self.client.login(
            email=self.teacher.user.email, password=self.teacher.user.password
        )
        self.client.get(reverse("teacher_delete", args=[self.teacher.pk]), follow=True)
        self.assertTemplateUsed("accounts/teacher_delete.html")

    def test_url_has_correct_reverse_url(self):
        self.assertEqual(
            reverse("teacher_delete", args=[self.teacher.pk]),
            "/accounts/teacher/delete/{}/".format(self.teacher.pk),
        )
