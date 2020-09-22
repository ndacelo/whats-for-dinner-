from django.contrib.auth import get_user_model
User = get_user_model()

import factory
import factory.fuzzy
from faker import Faker
from recipes import models


class IngredientSubCategoryFactory(factory.django.DjangoModelFactory):
    """ IngredientSubCategory Factory """

    class Meta:
        model = models.IngredientSubCategory

    name = factory.Faker('word')


class IngredientFactory(factory.django.DjangoModelFactory):
    """ Ingredient Factory """

    class Meta:
        model = models.Ingredient

    name = factory.Faker('word')
    category = factory.SubFactory(IngredientSubCategoryFactory)
    quantity = factory.fuzzy.FuzzyInteger(0,25)
    quantity_type = factory.Faker('word')


class UserFactory(factory.django.DjangoModelFactory):
    """ User Admin Factory """
    class Meta:
        model = User
    
    email = factory.Faker('email')
    username = factory.Faker('name')
    password = factory.Faker('word')

    is_superuser = True
    is_staff = True
    is_active = True


class RecipeFactory(factory.django.DjangoModelFactory):
    """ Recipe Factory """

    class Meta:
        model = models.Recipe

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    serving_size = factory.fuzzy.FuzzyInteger(1,6)
    prep_time = factory.fuzzy.FuzzyInteger(1,45)
    cook_time = factory.fuzzy.FuzzyInteger(1,1440)
    instructions = factory.Faker('text')

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)