# Generated by Django 3.0.2 on 2020-01-20 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190130_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('-pk',)},
        ),
    ]
