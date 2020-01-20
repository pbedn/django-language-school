# Generated by Django 2.1.5 on 2019-01-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses', to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='accounts.Student'),
        ),
    ]
