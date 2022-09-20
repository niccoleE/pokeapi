from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Pokemon(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image_url = models.URLField(max_length=2000)
    api_url = models.URLField(max_length=2000)
    types = ArrayField(models.CharField(max_length=200), blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owners = models.ManyToManyField(User, related_name='owners')

    def __str__(self):
        return self.name
