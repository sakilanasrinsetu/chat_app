from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="post_users"
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True, null=True
    )
    def __str__(self):
        return self.title

class Message(models.Model):
    # username = models.CharField(max_length=255)
    # room = models.CharField(max_length=255)
    # content = models.TextField()
    # date_added = models.DateTimeField(auto_now_add=True)

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recever =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user1")
    content = models.TextField()
    room = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)