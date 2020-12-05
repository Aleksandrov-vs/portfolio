from django.db import models
from markdownx.models import MarkdownxField
from domains.models import Domain


class Work(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=True, auto_created=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = MarkdownxField(max_length=500, null=True)
    photo = models.ImageField(upload_to='photo/%y', null=True)
    video = models.FileField(upload_to='video/%y', null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
