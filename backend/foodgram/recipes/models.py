from django.contrib.auth import get_user_model
from django.db import models

from ingredients.models import Ingredient
from tags.models import Tag

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe_images')
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)
    cooking_time = models.IntegerField()

    def __str__(self):
        return self.title
