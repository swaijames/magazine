# Generated by Django 4.1.1 on 2023-08-02 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg_blog', '0020_remove_comment_user_comment_name_comment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 13, 15, 58, 90151)),
        ),
    ]
