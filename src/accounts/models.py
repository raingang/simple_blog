from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, max_length=500, blank=True)
    location = models.CharField(null=True, max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user_image = models.ImageField(
        blank=True, upload_to="users_image/")

    def get_default_image_url(self):
        return '/media/users_image/default_user.png'
    def get_update_url(self):
    	return reverse('profile_update', args=[self.user.username])
    def get_absolute_url(self):
    	return reverse('profile', args = [self.user.username])
