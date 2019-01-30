# Generated by Django 2.1.5 on 2019-01-30 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                (
                    "type",
                    models.CharField(
                        choices=[("IN", "Individual"), ("GR", "Group")],
                        default="GR",
                        max_length=2,
                    ),
                ),
                ("number_of_lessons", models.IntegerField(default=1)),
                (
                    "students",
                    models.ManyToManyField(
                        related_name="courses", to="accounts.Student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("length", models.IntegerField()),
                (
                    "price_for_unit",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.Course"
                    ),
                ),
                (
                    "lector",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.Teacher",
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        related_name="lessons", to="accounts.Student"
                    ),
                ),
            ],
        ),
    ]
