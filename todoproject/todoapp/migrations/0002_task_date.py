# Generated by Django 4.2.2 on 2023-06-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-11-11'),
            preserve_default=False,
        ),
    ]
