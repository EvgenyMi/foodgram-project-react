from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='название тега',
    )
    color = models.CharField(
        max_length=7,
        verbose_name='цвет тега',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='url адрес для тега на английском',
    )

    class Meta:
        verbose_name = 'тег'

    def __str__(self):
        return self.name
