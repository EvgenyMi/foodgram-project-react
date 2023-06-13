from django.core.exceptions import ValidationError
import re


def validate_recipe_name(value):
    if not re.search(r'[a-zA-Zа-яА-Я]', value):
        raise ValidationError('Название рецепта должно содержать хотя бы одну букву.')
