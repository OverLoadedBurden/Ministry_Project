# Generated by Django 2.2.5 on 2020-03-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='research',
            field=models.BinaryField(default=None),
            preserve_default=False,
        ),
    ]