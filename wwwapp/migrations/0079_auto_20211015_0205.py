# Generated by Django 3.1.13 on 2021-10-15 00:05

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0078_auto_20211010_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 0, 5, 33, 798318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='name',
            field=models.CharField(default='post', max_length=100),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('([A-Z][a-z] [0-9])+')]),
        ),
    ]
