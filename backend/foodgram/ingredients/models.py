from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='название ингредиента',
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='единица измерения',
    )

    class Meta:
        verbose_name = 'ингредиент'

        constraints = (
            models.UniqueConstraint(
                fields=('name', 'measurement_unit'),
                name='unique_ingredient'
            ),
        )

    def __str__(self):
        return self.name
