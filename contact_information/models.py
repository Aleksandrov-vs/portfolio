from django.db import models
from domains.models import Domain

class ContactInformation(models.Model):
    phone_number = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=30)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
