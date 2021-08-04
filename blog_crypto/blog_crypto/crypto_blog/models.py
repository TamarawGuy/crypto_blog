from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100,
    )
    content = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )