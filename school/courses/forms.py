from django import forms
from .models import Course, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "type", "number_of_lessons", "students"]


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            "length",
            "price_for_unit",
            "date",
            "notes",
            "course",
            # "room",
            "lector",
            "students",
        ]
