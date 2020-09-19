from rest_framework import serializers
from recipes import models



class IngredientSubCategorySerializer(serializers.ModelSerializer):
    """ IngredientSubCategory Serializer """
    
    class Meta:
        model = models.IngredientSubCategory
        fields = ('name',)

class IngredientSerializer(serializers.ModelSerializer):
    """ Ingredient Serializer """
    category = IngredientSubCategorySerializer()
    class Meta:
        model = models.Ingredient
        fields = ('name', 'category', 'quantity', 'quantity_type')


class RecipeSerializer(serializers.ModelSerializer):
    """ Recipe Serializer """
    ingredients = IngredientSerializer(many=True)
    class Meta:
        
        model = models.Recipe
        fields = (
            'user', 'name', 'serving_size','prep_time','cook_time',
            'ingredients','instructions',
        )