# Generated by Django 3.1.13 on 2021-10-19 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0080_auto_20211017_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 20, 9, 3, 789533, tzinfo=utc)),
        ),
    ]
