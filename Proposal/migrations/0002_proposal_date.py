# Generated by Django 2.2.5 on 2019-12-27 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Proposal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
