# Generated by Django 2.2.7 on 2020-07-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20200707_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_task',
            name='priority_task',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
    ]
