# Generated by Django 3.1.13 on 2021-10-19 23:26

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0096_merge_20211019_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_page',
        ),
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 23, 26, 56, 675343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('([a-zA-Z0-9 ])+')]),
        ),
    ]
