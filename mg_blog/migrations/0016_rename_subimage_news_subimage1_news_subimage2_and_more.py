# Generated by Django 4.1.1 on 2023-08-01 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg_blog', '0015_news_decr1_news_decr2_news_decr3_news_decr4_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='subimage',
            new_name='subimage1',
        ),
        migrations.AddField(
            model_name='news',
            name='subimage2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 36, 15, 705046)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 36, 15, 705046)),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 36, 15, 706044)),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 13, 36, 15, 706044)),
        ),
    ]
