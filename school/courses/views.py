from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Course, Lesson
from .forms import CourseForm, LessonForm


class CourseListView(ListView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm


class LessonListView(ListView):
    model = Lesson


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm


class LessonDetailView(DetailView):
    model = Lesson


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
