# Generated by Django 4.2.4 on 2024-01-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-08-24'),
            preserve_default=False,
        ),
    ]
