# Generated by Django 3.0.2 on 2020-01-20 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20200120_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
    ]