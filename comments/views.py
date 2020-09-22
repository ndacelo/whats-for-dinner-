from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from comments import serializers
from comments.models import ReComment, RecipeComment



class RecipeCommentViewSet(viewsets.ModelViewSet):
    """ RecipeComment viewset """
    queryset = RecipeComment.objects.all()
    serializer_class = serializers.RecipeCommentSerializer

class ReCommentViewSet(viewsets.ModelViewSet):
    """ ReComment viewset """
    queryset = ReComment.objects.all()
    serializer_class = serializers.ReCommentSerializer


