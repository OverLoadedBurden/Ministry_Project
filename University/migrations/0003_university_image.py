# Generated by Django 2.2.5 on 2019-12-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0002_auto_20191227_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.BinaryField(default=None),
            preserve_default=False,
        ),
    ]