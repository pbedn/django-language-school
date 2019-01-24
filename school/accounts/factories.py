import factory
from factory.django import DjangoModelFactory
from faker import Factory
from django.contrib.auth import get_user_model

from school.accounts.models import Student, Teacher

faker = Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = faker.email()
    password = 'pass'


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)
    first_name = faker.first_name()
    last_name = faker.last_name()


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
    first_name = faker.first_name()
    last_name = faker.last_name()
    phone = faker.phone_number()
