from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    thumb = models.URLField(max_length=200, blank=True, null=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    posted = models.DateTimeField(auto_now_add=True,null=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    posted = models.DateTimeField(auto_now_add=True,null=True)