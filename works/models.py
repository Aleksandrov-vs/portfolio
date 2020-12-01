from django.db import models


class Work(models.Model):

    id = models.IntegerField(primary_key=True, null=False, blank=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=500, null=True)
    photo = models.ImageField(upload_to='photo/%y', null=True)
    video = models.FileField(upload_to='video/%y', null=True)

    def __str__(self):
        return self.name
