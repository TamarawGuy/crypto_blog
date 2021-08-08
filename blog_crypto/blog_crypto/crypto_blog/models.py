from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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


class Like(models.Model):
    blog = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
