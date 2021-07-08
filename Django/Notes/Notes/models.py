from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField(null=True)
    content = models.TextField(null=True)

