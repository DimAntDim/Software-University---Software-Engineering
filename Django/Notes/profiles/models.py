from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True)
    image_url = models.URLField(null=True)
