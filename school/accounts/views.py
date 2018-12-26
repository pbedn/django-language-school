from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, StudentCreationForm, TeacherCreationForm, StudentForm, TeacherForm
from .models import Student, Teacher


class SignUpCreateView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = StudentCreationForm
    template_name = 'accounts/student_form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('student_update', pk=form.instance.student.pk)


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = TeacherCreationForm
    template_name = 'accounts/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('teacher_update', pk=form.instance.teacher.pk)


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teacher_list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher_list')
