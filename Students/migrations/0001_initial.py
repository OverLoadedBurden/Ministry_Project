# Generated by Django 2.2.5 on 2020-03-15 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('collage_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ph', models.IntegerField(unique=True)),
                ('research', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Research.Research')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
    ]
