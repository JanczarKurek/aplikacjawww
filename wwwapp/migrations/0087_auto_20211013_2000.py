# Generated by Django 3.1.13 on 2021-10-13 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0086_auto_20211013_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 18, 0, 48, 137656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
