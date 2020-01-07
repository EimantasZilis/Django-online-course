from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    # Associate new model with User class
    # Any extra attributes will be extending user class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Upload to specified output directory within media folder.
    # 'profile_pics'  needs to exist
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

