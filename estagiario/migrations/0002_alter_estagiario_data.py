# Generated by Django 4.0.5 on 2022-06-10 00:20

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagiario',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 0, 20, 40, 620920, tzinfo=utc)),
        ),
    ]