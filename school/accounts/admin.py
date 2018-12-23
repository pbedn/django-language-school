from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from. models import CustomUser, Student, Teacher


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('display_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'display_name', 'is_staff')
    search_fields = ('email', 'display_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
