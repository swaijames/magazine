# Generated by Django 4.1.1 on 2023-07-24 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg_blog', '0011_category_category_image_alter_category_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 14, 55, 51, 84540)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 14, 55, 51, 84540)),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 14, 55, 51, 84540)),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 14, 55, 51, 84540)),
        ),
    ]