# Generated by Django 4.0.4 on 2022-05-29 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='session',
            new_name='admission_session',
        ),
    ]
