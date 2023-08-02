from django.db import models
from datetime import datetime

from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category_image = models.FileField(blank=False, upload_to='category/')
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(default=datetime.today())

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class news(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    decr1 = models.TextField(blank=True, null=True)
    decr2 = models.TextField(blank=True, null=True)
    decr3 = models.TextField(blank=True, null=True)
    decr4 = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=False, null=False)
    image = models.FileField(blank=False, null=False)
    subimage1 = models.FileField(blank=True, null=True)
    subimage2 = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(default=datetime.today())

    class Meta:
        verbose_name_plural = "News"
        get_latest_by = "created_at"

    def __str__(self):
        return self.title


class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(news, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.today())
    updated_at = models.DateTimeField(default=datetime.today())

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment
