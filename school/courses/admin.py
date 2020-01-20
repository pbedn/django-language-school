from django.contrib import admin
from django import forms
from .models import Course, Lesson


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ["name", "type", "number_of_lessons"]
    readonly_fields = ["name", "type", "number_of_lessons"]


admin.site.register(Course, CourseAdmin)


class LessonAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm
    list_display = ["length", "price_for_unit", "date", "notes"]
    readonly_fields = ["length", "price_for_unit", "date", "notes"]


admin.site.register(Lesson, LessonAdmin)
