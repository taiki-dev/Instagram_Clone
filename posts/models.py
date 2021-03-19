from django.contrib.auth.models import User
from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
