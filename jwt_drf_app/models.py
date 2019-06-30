from django.db import models


class Post(models.Model):

    class Meta:
        ordering = ("-created",)

    author = models.ForeignKey("auth.User", related_name="posts",
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    likes_count = models.IntegerField(default=0)
