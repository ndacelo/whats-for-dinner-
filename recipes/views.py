from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from recipes import serializers
from recipes import models



class RecipeViewSet(viewsets.ModelViewSet):
    """ Recipe viewset """

    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    """ Ingredient viewset """

    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    """ Recipe Ingredient viewset """

    queryset = models.RecipeIngredient.objects.all()
    serializer_class = serializers.RecipeIngredientSerializer

class IngredientSubCategoryViewSet(viewsets.ModelViewSet):
    """ Ingredient SubCategory viewset """
    queryset = models.IngredientSubCategory.objects.all()
    serializer_class = serializers.IngredientSubCategorySerializer

class IngredientCategoryViewSet(viewsets.ModelViewSet):
    """ Ingredient SubCategory viewset """
    queryset = models.IngredientCategory.objects.all()
    serializer_class = serializers.IngredientCategorySerializer
