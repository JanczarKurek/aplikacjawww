# Generated by Django 3.1.13 on 2021-10-13 18:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0089_auto_20211013_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 13, 18, 22, 36, 505805, tzinfo=utc)),
        ),
    ]
