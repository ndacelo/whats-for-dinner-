from django.contrib import admin
from comments import models
# Register your models here.


@admin.register(models.RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):

    list_display = ('comment', 'user', 'likes', 'dislikes', 'replies')
    readonly_fields = ( 'dislikes', 'likes', 'replies')

    def replies(self, obj):
        return obj.get_total_comments

    def likes(self, obj):
        return obj.get_total_likes

    def dislikes(self, obj):
        return obj.get_total_dislikes    


@admin.register(models.ReComment)
class ReCommentAdmin(admin.ModelAdmin):

    list_display = ('comment', 'user', 'likes', 'dislikes', 'replies')
    readonly_fields = ('replies', 'dislikes', 'likes')

    def replies(self, obj):
        return obj.get_total_replies

    def likes(self, obj):
        return obj.get_total_likes

    def dislikes(self, obj):
        return obj.get_total_dislikes    