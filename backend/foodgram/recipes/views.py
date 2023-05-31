from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import RecipeFilter
from .models import Recipe
from .permissions import IsAuthorOrAdminPermission
from .serializers import CreateUpdateRecipeSerializer, RecipeSerializer
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
