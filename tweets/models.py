from django.db import models
from user.models import User


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="", blank=True)
    likes = models.ManyToManyField(
        User, related_name="tweet_user", blank=True, through=TweetLike
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Tweet."""

        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"

    def __str__(self):
       return self.content[:10]
