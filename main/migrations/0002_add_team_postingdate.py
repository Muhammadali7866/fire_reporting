# Generated by Django 4.0.6 on 2022-10-03 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_team',
            name='postingDate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 3, 9, 13, 34, 816630, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
