from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentCreationForm, TeacherCreationForm, StudentForm, TeacherForm
from .models import Student, Teacher


class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentCreateView(LoginRequiredMixin, View):
    user_form_class = StudentCreationForm
    student_form_class = StudentForm
    template_name = 'accounts/student_form.html'

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.GET or None)
        student_form = self.student_form_class(request.GET or None)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'student_form': student_form})

    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(request.POST or None)
        student_form = self.student_form_class(request.POST or None)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student = student_form.save(commit=False)
            student.user_id = user_form.instance.pk
            student.save()
            return redirect('student_detail', pk=student_form.instance.pk)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'student_form': student_form})


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student


class StudentUpdateView(LoginRequiredMixin, View):
    user_form_class = StudentCreationForm
    student_form_class = StudentForm
    template_name = 'accounts/student_form.html'
    success_url = reverse_lazy('student_list')

    def get(self, request, pk, *args, **kwargs):
        student_instance = get_object_or_404(Student, pk=pk)
        user_instance = get_user_model().objects.get(pk=student_instance.user.pk)
        user_form = self.user_form_class(request.GET or None, instance=user_instance)
        student_form = self.student_form_class(request.GET or None, instance=student_instance)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'student_form': student_form})

    def post(self, request, pk, *args, **kwargs):
        student_instance = get_object_or_404(Student, pk=pk)
        user_instance = get_object_or_404(get_user_model(), pk=student_instance.user.pk)
        user_form = self.user_form_class(request.POST or None, instance=user_instance)
        student_form = self.student_form_class(request.POST or None, instance=student_instance)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student = student_form.save(commit=False)
            student.user_id = user_form.instance.pk
            student.save()
            return redirect(reverse_lazy('student_list'))
        return render(request, self.template_name, {'user_form': user_form,
                                                    'student_form': student_form})


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
        user_form = self.user_form_class(request.POST or None)
        teacher_form = self.teacher_form_class(request.POST or None)
        if user_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user_id = user_form.instance.pk
            teacher.save()
            return redirect('teacher_detail', pk=teacher_form.instance.pk)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'teacher_form': teacher_form})


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher


class TeacherUpdateView(LoginRequiredMixin, View):
    user_form_class = TeacherCreationForm
    teacher_form_class = TeacherForm
    template_name = 'accounts/teacher_form.html'
    # success_url = reverse_lazy('teacher_list')

    def get(self, request, pk, *args, **kwargs):
        teacher_instance = get_object_or_404(Teacher, pk=pk)
        user_instance = get_object_or_404(get_user_model(), pk=teacher_instance.user.pk)
        user_form = self.user_form_class(request.GET or None, instance=user_instance)
        teacher_form = self.teacher_form_class(request.GET or None, instance=teacher_instance)
        return render(request, self.template_name, {'user_form': user_form,
                                                    'teacher_form': teacher_form})

    def post(self, request, pk, *args, **kwargs):
        teacher_instance = get_object_or_404(Teacher, pk=pk)
        user_instance = get_object_or_404(get_user_model(), pk=teacher_instance.user.pk)
        user_form = self.user_form_class(request.POST or None, instance=user_instance)
        teacher_form = self.teacher_form_class(request.POST or None, instance=teacher_instance)
        if user_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user_id = user_form.instance.pk
            teacher.save()
            return redirect(reverse_lazy('teacher_list'))
        return render(request, self.template_name, {'user_form': user_form,
                                                    'teacher_form': teacher_form})


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher_list')
