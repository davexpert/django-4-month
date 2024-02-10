from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.png')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class EMAILCodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Code {self.code} for user {self.user.username}'
