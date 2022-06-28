from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


from posts.models import Post

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reactions = ArrayField(models.CharField(max_length=2000))