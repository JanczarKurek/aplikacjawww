# Generated by Django 3.1.13 on 2021-10-13 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0079_auto_20211013_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='matura_exam_year',
        ),
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 16, 31, 57, 842700, tzinfo=utc)),
        ),
    ]
