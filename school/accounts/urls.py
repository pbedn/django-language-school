from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
]

urlpatterns += (
    # urls for Student
    path('student/', views.StudentListView.as_view(), name='student_list'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
)

urlpatterns += (
    # urls for Teacher
    path('teacher/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teacher/detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/update/<int:pk>/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher/delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
)
