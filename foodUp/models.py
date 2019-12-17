from django.db import models
from django.utils import timezone
from users.models import User, Profile


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='%(class)s_receiver')
    com = models.TextField()
