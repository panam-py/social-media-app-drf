from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


# Create your models here.
class Media(models.Model):
    type = models.CharField(max_length=30)
    source = models.CharField(max_length=2000)


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reactions = ArrayField(models.CharField(max_length=2000))
    text_content = models.TextField()
    media = ArrayField(models.CharField(max_length=2000))
    date_posted = models.DateTimeField(auto_now_add=True)
