# Generated by Django 2.2.7 on 2020-07-04 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20200703_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='user_project',
            name='progress_percent',
        ),
    ]
