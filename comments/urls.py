from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comments import views

router = DefaultRouter()
router.register('replies', views.ReCommentViewSet)
router.register('recipe_comments', views.RecipeCommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]