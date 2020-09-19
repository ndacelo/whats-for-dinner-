from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from recipes import serializers
from recipes.models import Recipe, Ingredient, IngredientSubCategory



class RecipeViewSet(viewsets.ModelViewSet):
    """ Recipe viewset """
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    """ Ingredient viewset """
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class IngredientSubCategoryViewSet(viewsets.ModelViewSet):
    """ IngredientSubCategory viewset """
    queryset = IngredientSubCategory.objects.all()
    serializer_class = serializers.IngredientSubCategorySerializer
