# Generated by Django 2.2.5 on 2020-02-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0011_research_unv'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='degree',
            field=models.CharField(default=None, max_length=55),
            preserve_default=False,
        ),
    ]
