from rest_framework import serializers
from comments import models




class CommentBaseSerializer(serializers.ModelSerializer):
    """ CommentBase Serializer """

    class Meta:
        model = models.CommentBase
        fields = ('comment',)



class ReCommentSerializer(serializers.ModelSerializer):
    """ ReComment Serializer """

    # original_comment = CommentBaseSerializer()
    
    class Meta:
        model = models.ReComment
        fields = ('user', 'comment', 'original_comment',)



class RecipeCommentSerializer(serializers.ModelSerializer):
    """ RecipeComment Serializer """

    class Meta:
        model = models.RecipeComment
        fields = ('user', 'comment', 'original_post')

