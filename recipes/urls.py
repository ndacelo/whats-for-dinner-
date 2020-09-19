from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('ingredients_subcategory', views.IngredientSubCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]