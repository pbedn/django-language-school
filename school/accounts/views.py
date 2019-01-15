from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, View, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect

from .forms import StudentCreationForm, TeacherCreationForm, StudentForm, TeacherForm
from .models import Student, Teacher


class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentCreateView(LoginRequiredMixin, View):
    user_form_class = StudentCreationForm
    student_form_class = StudentForm
    template_name = 'accounts/student_form.html'

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class()
        student_form = self.student_form_class()
        return render(request, self.template_name, {'user_form': user_form,
                                                    'student_form': student_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST)
        student_form = self.student_form_class(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student = student_form.save(commit=False)
            student.user_id = user_form.instance.pk
            student.save()
            return redirect('student_detail', pk=student_form.instance.pk)
        else:
            return redirect('student_create')


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


class TeacherCreateView(LoginRequiredMixin, View):
    user_form_class = TeacherCreationForm
    teacher_form_class = TeacherForm
    template_name = 'accounts/teacher_form.html'

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.GET or None)
        teacher_form = self.teacher_form_class(request.GET or None)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'teacher_form': teacher_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST)
        teacher_form = self.teacher_form_class(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user_id = user_form.instance.pk
            teacher.save()
            return redirect('teacher_detail', pk=teacher_form.instance.pk)
        else:
            return redirect('teacher_create')


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teacher_list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher_list')
