# Generated by Django 3.2.13 on 2022-05-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-05-15'),
            preserve_default=False,
        ),
    ]
