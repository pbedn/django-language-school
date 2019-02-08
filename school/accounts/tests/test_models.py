from django.test import TestCase
from django.contrib.auth import get_user_model

from school.accounts.factories import UserFactory, StudentFactory, TeacherFactory
from school.accounts.models import Student, Teacher, CustomUser


class CustomUserModelTest(TestCase):
    """
    Tests for the CustomUser model
    """

    def setUp(self):
        self.user = UserFactory()

    def test_user_is_created(self):
        user = get_user_model().objects.first()
        self.assertEqual(user.email, "user0@example.com")
        self.assertEqual(user.password, "pass")

    def test_create_user(self):
        user = CustomUser.objects.create_user(email="test@example.com", password="pass")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("pass"))
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email="test@example.com", password="pass"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("pass"))
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)

    def test_create_user_with_empty_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email="")

    def test_create_superuser_with_wrong_fields(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email="test@example.com", password="pass", is_staff=False
            )
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email="test@example.com", password="pass", is_superuser=False
            )

    def tearDown(self):
        UserFactory.reset_sequence()


class StudentModelTest(TestCase):
    """
    Tests for the Student model
    """

    def setUp(self):
        user = UserFactory()
        self.student = StudentFactory(user=user)

    def test_student_is_created(self):
        student = Student.objects.first()
        self.assertEqual(student.user.email, "user0@example.com")
        self.assertEqual(student.user.password, "pass")
        self.assertEqual(student.first_name, "Student0")
        self.assertEqual(student.last_name, "LastName")
        object_display = student.first_name + " " + student.last_name
        self.assertEqual(str(student), object_display)

    def test_student_is_deleted(self):
        student = Student.objects.first()
        self.assertEqual(Student.objects.count(), 1)
        student.delete()
        self.assertEqual(Student.objects.count(), 0)

    def test_student_is_deleted_but_user_is_wrong(self):
        student = Student.objects.first()
        student.user_id = 2
        student.save()
        self.assertEqual(Student.objects.count(), 1)
        with self.assertRaises(CustomUser.DoesNotExist):
            student.delete()
        self.assertEqual(Student.objects.count(), 0)

    def tearDown(self):
        UserFactory.reset_sequence()
        StudentFactory.reset_sequence()


class TeacherModelTest(TestCase):
    """
    Tests for the Teacher model
    """

    def setUp(self):
        user = UserFactory()
        self.teacher = TeacherFactory(user=user)

    def test_teacher_is_created(self):
        teacher = Teacher.objects.first()
        self.assertEqual(teacher.user.email, "user0@example.com")
        self.assertEqual(teacher.user.password, "pass")
        self.assertEqual(teacher.first_name, "Teacher0")
        self.assertEqual(teacher.last_name, "LastName")
        object_display = teacher.first_name + " " + teacher.last_name
        self.assertEqual(str(teacher), object_display)

    def test_teacher_is_deleted(self):
        teacher = Teacher.objects.first()
        self.assertEqual(Teacher.objects.count(), 1)
        teacher.delete()
        self.assertEqual(Teacher.objects.count(), 0)

    def test_teacher_is_deleted_but_user_is_wrong(self):
        teacher = Teacher.objects.first()
        teacher.user_id = 2
        teacher.save()
        self.assertEqual(Teacher.objects.count(), 1)
        with self.assertRaises(CustomUser.DoesNotExist):
            teacher.delete()
        self.assertEqual(Teacher.objects.count(), 0)

    def tearDown(self):
        UserFactory.reset_sequence()
        TeacherFactory.reset_sequence()
