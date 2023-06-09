from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import RecipeFilter
from .models import Favorite, Recipe, RecipeIngredient, ShoppingList
from .permissions import IsAuthorOrAdminPermission
from .serializers import (BriefRecipeSerializer, CreateUpdateRecipeSerializer, 
                          RecipeSerializer)
from ingredients.models import Ingredient
from users.pagination import CustomPageNumberPagination


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    filterset_class = RecipeFilter
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthorOrAdminPermission,)

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CreateUpdateRecipeSerializer
        return RecipeSerializer

    @action(detail=True, methods=('post', 'delete'))
    def favorite(self, request, pk=None):
        user = self.request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        if self.request.method == 'POST':
            if Favorite.objects.filter(user=user, recipe=recipe).exists():
                raise exceptions.ValidationError(
                    'Рецепт уже добавлен в избранное')

            Favorite.objects.create(user=user, recipe=recipe)
            serializer = BriefRecipeSerializer(
                recipe, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if self.request.method == 'DELETE':
            favorite = get_object_or_404(Favorite, user=user, recipe=recipe)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=('post', 'delete'))
    def shopping_cart(self, request, pk=None):
        user = self.request.user
        recipe = get_object_or_404(Recipe, pk=pk)

        if self.request.method == 'POST':
            if ShoppingList.objects.filter(user=user, recipe=recipe).exists():
                raise exceptions.ValidationError(
                    'Ингредиенты рецепта уже добавлены в список покупок')

            ShoppingList.objects.create(user=user, recipe=recipe)
            serializer = BriefRecipeSerializer(
                recipe, context={'request': request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if self.request.method == 'DELETE':
            if not ShoppingList.objects.filter(user=user, recipe=recipe).exists():
                raise exceptions.ValidationError(
                    'Нельзя удалить недобавенные ингредиенты рецепта')

            shopping_list = get_object_or_404(ShoppingList, user=user, recipe=recipe)
            shopping_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=('get',), permission_classes=(IsAuthenticated,))
    def loading_shopping_cart(self, request):
        shopping_cart = ShoppingList.objects.filter(user=request.user)
        recipes = [item.recipe.id for item in shopping_cart]
        grocery_list = RecipeIngredient.objects.filter(
            recipes__in=recipes
        ).values('ingredient').annotate(amount=Sum('amount'))

        grocery_list_text = 'Ваш список покупок для приготовления по рецептам \n\n'
        for item in grocery_list:
            ingredient = Ingredient.objects.get(pk=item['ingredient'])
            amount = item['amount']
            grocery_list_text += f'{ingredient.name}: {amount} {ingredient.measurement_unit}\n'
        response = HttpResponse(grocery_list_text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=grocery_list.txt'
        return response
