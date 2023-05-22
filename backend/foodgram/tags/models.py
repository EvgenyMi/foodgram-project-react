from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_code = models.CharField(max_length=7)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
