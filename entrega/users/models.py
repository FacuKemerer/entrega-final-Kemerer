from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True, default='avatares/Avatar.png')

    def __str__(self):
        return f"{self.user} - {self.avatar}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'