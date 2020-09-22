import factory
import factory.fuzzy
from faker import Faker
from comments import models

from recipes.factories import UserFactory, RecipeFactory



class CommentBaseFactory(factory.django.DjangoModelFactory):
    """ Comment Base Factory """
    class Meta:
        model = models.CommentBase

    user = factory.SubFactory(UserFactory)
    comment = factory.Faker('text')



class ReCommentFactory(CommentBaseFactory):
    """ ReComment Factory """
    class Meta:
        model = models.ReComment

    original_comment = factory.SubFactory(CommentBaseFactory)



class RecipeCommentFactory(CommentBaseFactory):
    """ Comment on a recipe """
    class Meta:
        model = models.RecipeComment

    original_post = factory.SubFactory(RecipeFactory)