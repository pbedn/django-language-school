from django.urls import path

from . import views

urlpatterns = (
    # urls for Course
    path("course/", views.CourseListView.as_view(), name="course_list"),
    path("course/create/", views.CourseCreateView.as_view(), name="course_create"),
    path(
        "course/detail/<int:pk>/",
        views.CourseDetailView.as_view(),
        name="course_detail",
    ),
    path(
        "course/update/<int:pk>/",
        views.CourseUpdateView.as_view(),
        name="course_update",
    ),
)

urlpatterns += (
    # urls for Lesson
    path("lesson/", views.LessonListView.as_view(), name="lesson_list"),
    path("lesson/create/", views.LessonCreateView.as_view(), name="lesson_create"),
    path(
        "lesson/detail/<int:pk>/",
        views.LessonDetailView.as_view(),
        name="lesson_detail",
    ),
    path(
        "lesson/update/<int:pk>/",
        views.LessonUpdateView.as_view(),
        name="lesson_update",
    ),
)
