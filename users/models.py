import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
