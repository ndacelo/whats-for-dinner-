from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class IngredientSubCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(IngredientSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField(default=0)
    quantity_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    @property
    def all_instances(self):
        return Recipe.objects.filter(ingredients=self).count()

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    serving_size = models.IntegerField(default=1)
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()

    def __str__(self):
        return self.name

    @property
    def get_total_likes(self):
        return self.like.user.count()

    @property
    def get_total_dislikes(self):
        return self.dislike.user.count()

    @property
    def get_total_comments(self):
        return self.comment.count()