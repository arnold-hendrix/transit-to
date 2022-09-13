from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django_jsonfield_backport.models import JSONField


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Favourites(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    locations = JSONField()
