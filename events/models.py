from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.TextField(max_length=100, null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False)
    free = models.BooleanField(default=True)

    def __str__(self):
        return self.name
