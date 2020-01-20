from django.db import models
from django.urls import reverse

INDIVIDUAL = "IN"
GROUP = "GR"

COURSE_TYPE = ((INDIVIDUAL, "Individual"), (GROUP, "Group"))


class Course(models.Model):
    """Represents single course"""

    name = models.CharField(blank=False, null=False, max_length=150)
    type = models.CharField(max_length=2, choices=COURSE_TYPE, default=GROUP)
    number_of_lessons = models.IntegerField(default=1, blank=False, null=False)

    # students signed to course
    students = models.ManyToManyField(
        "accounts.Student", related_name="courses", blank=True
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('course_update', args=(self.pk,))


class Lesson(models.Model):
    """Represents single lesson"""

    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    length = models.IntegerField(blank=False, null=False)

    price_for_unit = models.DecimalField(
        blank=False, null=False, default=0.0, decimal_places=2, max_digits=10
    )

    date = models.DateTimeField(null=True, blank=True)
    # room = models.ForeignKey('Room', null=True, blank=True, on_delete=models.SET_NULL)
    lector = models.ForeignKey(
        "accounts.Teacher", null=True, blank=True, on_delete=models.SET_NULL
    )
    notes = models.TextField(null=True, blank=True)

    # students present during the lesson
    students = models.ManyToManyField(
        "accounts.Student", related_name="lessons", blank=True
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        """String for representing the Model object."""
        return self.course.name + ' - Lesson: ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('lesson_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('lesson_update', args=(self.pk,))

    def get_total_price(self):
        """Return total price for all lessons"""
        return self.price_for_unit * self.course.number_of_lessons
