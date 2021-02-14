from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes.views import (RecipeIngredientViewSet, RecipeViewSet, IngredientViewSet, IngredientSubCategoryViewSet,
RecipeIngredientViewSet, IngredientCategoryViewSet)
from comments.views import RecipeCommentViewSet, ReCommentViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('recipe_ingredients', RecipeIngredientViewSet)
router.register('ingredients', IngredientViewSet)
router.register('ingredients_category', IngredientCategoryViewSet)
router.register('ingredients_subcategory', IngredientSubCategoryViewSet)
router.register('replies', ReCommentViewSet)
router.register('recipe_comments', RecipeCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]