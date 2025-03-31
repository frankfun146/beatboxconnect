from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class ContactForm(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    comments = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
