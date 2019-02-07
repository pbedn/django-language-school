import factory
from factory.django import DjangoModelFactory
from faker import Factory
from django.contrib.auth import get_user_model

from school.accounts.models import Student, Teacher

faker = Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = "pass"


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)
    first_name = factory.Sequence(lambda n: 'Student{0}'.format(n))
    last_name = 'LastName'


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
    first_name = factory.Sequence(lambda n: 'Teacher{0}'.format(n))
    last_name = 'LastName'
    phone = faker.phone_number()
