from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('dashboard', args=[self.username])
