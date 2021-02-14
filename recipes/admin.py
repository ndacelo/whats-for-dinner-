from django.contrib import admin
from recipes import models
# Register your models here.



@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ "Recipe Admin """


    list_display = ('name', 'serving_size', 'comments', 'likes', 'dislikes')
    readonly_fields = ('comments', 'likes', 'dislikes')

    def comments(self, obj):
        return obj.get_total_comments

    def likes(self, obj):
        return obj.get_total_likes

    def dislikes(self, obj):
        return obj.get_total_dislikes    


@admin.register(models.IngredientSubCategory)
class IngredientSubCategoryAdmin(admin.ModelAdmin):
    """ IngredientSubCategory Admin """

    class Meta:
        model = models.IngredientSubCategory
        fields = '__all__'

@admin.register(models.IngredientCategory)
class IngredientCategoryAdmin(admin.ModelAdmin):
    """ IngredientCategory Admin """

    class Meta:
        model = models.IngredientCategory
        fields = '__all__'


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Ingredient Admin """

    fields = ['name', 'category', 'sub_category']
    list_display = ('name', 'category', 'in_recipes')
    readonly_fields = ('in_recipes',)

    def in_recipes(self, obj):
        return obj.all_instances


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    """ RecipeIngredient Admin """
    
    fields = ['ingredient', 'prepared', 'quantity', 'quantity_type']
    list_display = ('ingredient', 'quantity')

