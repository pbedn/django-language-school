# from django.urls import reverse
# from django.test import TestCase
# from .models import Course, Lesson
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
# from django.contrib.contenttypes.models import ContentType
#
#
#
# class CourseViewTest(TestCase):
#     '''
#     Tests for Course
#     '''
#     def setUp(self):
#         self.client = Client()
#
#     def test_list_course(self):
#         url = reverse('app_name_course_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_create_course(self):
#         url = reverse('app_name_course_create')
#         data = {
#             "name": "name",
#             "type": "type",
#             "number_of_lessons": "number_of_lessons",
#             "students": create_'student'().pk,
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 302)
#
#     def test_detail_course(self):
#         course = create_course()
#         url = reverse('app_name_course_detail', args=[course.pk,])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_course(self):
#         course = create_course()
#         data = {
#             "name": "name",
#             "type": "type",
#             "number_of_lessons": "number_of_lessons",
#             "students": create_'student'().pk,
#         }
#         url = reverse('app_name_course_update', args=[course.pk,])
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)
#
#
# class LessonViewTest(unittest.TestCase):
#     '''
#     Tests for Lesson
#     '''
#     def setUp(self):
#         self.client = Client()
#
#     def test_list_lesson(self):
#         url = reverse('app_name_lesson_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_create_lesson(self):
#         url = reverse('app_name_lesson_create')
#         data = {
#             "length": "length",
#             "price_for_unit": "price_for_unit",
#             "date": "date",
#             "notes": "notes",
#             "course": create_'course'().pk,
#             "room": create_'room'().pk,
#             "lector": create_'teacher'().pk,
#             "students": create_'student'().pk,
#         }
#         response = self.client.post(url, data=data)
#         self.assertEqual(response.status_code, 302)
#
#     def test_detail_lesson(self):
#         lesson = create_lesson()
#         url = reverse('app_name_lesson_detail', args=[lesson.pk,])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_lesson(self):
#         lesson = create_lesson()
#         data = {
#             "length": "length",
#             "price_for_unit": "price_for_unit",
#             "date": "date",
#             "notes": "notes",
#             "course": create_'course'().pk,
#             "room": create_'room'().pk,
#             "lector": create_'teacher'().pk,
#             "students": create_'student'().pk,
#         }
#         url = reverse('app_name_lesson_update', args=[lesson.pk,])
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)
