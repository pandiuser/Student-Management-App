# Generated by Django 5.1 on 2024-08-25 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_numner',
            new_name='student_number',
        ),
    ]
