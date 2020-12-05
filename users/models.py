from django.db import models
from django.contrib.auth.models import AbstractUser
from domains.models import Domain


class User(AbstractUser):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
