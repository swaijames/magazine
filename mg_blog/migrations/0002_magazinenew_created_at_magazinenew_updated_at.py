# Generated by Django 4.1.1 on 2023-07-20 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazinenew',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 12, 39, 39, 483529)),
        ),
        migrations.AddField(
            model_name='magazinenew',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 12, 39, 39, 483529)),
        ),
    ]
