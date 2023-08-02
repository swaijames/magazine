# Generated by Django 4.1.1 on 2023-07-20 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg_blog', '0010_alter_news_options_alter_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.FileField(default='', upload_to='category/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 16, 15, 13, 494161)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 16, 15, 13, 494161)),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 16, 15, 13, 495156)),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 16, 15, 13, 495156)),
        ),
    ]
