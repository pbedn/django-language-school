from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Represents custom user"""

    username = None
    first_name = None
    last_name = None
    email = models.EmailField("email address", unique=True)
    display_name = models.CharField(blank=True, max_length=30)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Student(models.Model):
    """This model represents single student"""

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    first_name = models.CharField(blank=False, null=False, max_length=20)
    last_name = models.CharField(blank=False, null=False, max_length=20)

    # additional - not required
    phone = models.CharField(max_length=9, blank=True, null=True)
    general_discount = models.PositiveSmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # invoice data - note required
    company_name = models.CharField(blank=True, null=True, max_length=50)
    company_address = models.TextField(blank=True, null=True, max_length=100)
    company_tax_number = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        ordering = ("pk",)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("student_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("student_update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("student_delete", args=(self.pk,))

    def delete(self, using=None, keep_parents=False):
        """Delete Student object and related CustomUser"""
        super().delete()
        self.user.delete()

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name + " " + self.last_name


class Teacher(models.Model):
    """Represents single teacher"""

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    first_name = models.CharField(blank=False, null=False, max_length=20)
    last_name = models.CharField(blank=False, null=False, max_length=20)
    phone = models.CharField(max_length=9, blank=False, null=False)

    # additional - not required
    notes = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    basic_course_rate = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2
    )
    basic_individual_lesson_rate = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2
    )

    class Meta:
        ordering = ("pk",)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("teacher_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("teacher_update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("teacher_delete", args=(self.pk,))

    def delete(self, using=None, keep_parents=False):
        """Delete Teacher object and related CustomUser"""
        super().delete()
        self.user.delete()

    def __str__(self):
        """String for representing the Model object."""
        return self.first_name + " " + self.last_name
