from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from .models import CustomUser, Student, Teacher


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "display_name")


class StudentCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        password = CustomUser.objects.make_random_password()
        user.set_password(password)
        user.save()
        return user


class StudentForm(ModelForm):
    phone = forms.CharField(min_length=9, max_length=9)
    company_tax_number = forms.CharField(min_length=10)

    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "phone",
            "general_discount",
            "date_of_birth",
            "company_name",
            "company_address",
            "company_tax_number",
        )
        widgets = {
            "phone": forms.NumberInput(),
            "date_of_birth": forms.DateInput(
                attrs={'type': 'date'}
            ),
            "company_tax_number": forms.NumberInput(),
        }


class TeacherCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        password = CustomUser.objects.make_random_password()
        user.set_password(password)
        user.save()
        return user


class TeacherForm(ModelForm):
    phone = forms.CharField(min_length=9, max_length=9)

    class Meta:
        model = Teacher
        fields = (
            "first_name",
            "last_name",
            "phone",
            "notes",
            "date_of_birth",
            "basic_course_rate",
            "basic_individual_lesson_rate",
        )
        widgets = {
            "phone": forms.NumberInput(),
            "date_of_birth": forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
