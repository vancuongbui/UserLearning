from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    #additional classes
    portfolioSite = models.URLField(blank = True)

    profilePics = models.ImageField(upload_to = "media/profilePics", blank=True)

    def __str__(self):
        return self.user.username
