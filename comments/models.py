from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from recipes.models import Recipe




class CommentBase(models.Model):
    """ Comment Model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class ReComment(CommentBase):
    """ Comment to a comment """

    original_comment = models.ForeignKey(CommentBase, related_name='re', on_delete=models.CASCADE)

    @property
    def get_total_replies(self):
        return self.re.count()

    @property
    def get_total_likes(self):
        return self.like.user.count()

    @property
    def get_total_dislikes(self):
        return self.dislike.user.count()


class RecipeComment(CommentBase):
    """ Comment on a recipe """

    original_post = models.ForeignKey(Recipe, related_name='comment', on_delete=models.CASCADE)

    @property
    def get_total_comments(self):
        return self.re.count()

    @property
    def get_total_likes(self):
        return self.like.user.count()

    @property
    def get_total_dislikes(self):
        return self.dislike.user.count()


class CommentLike(models.Model):
    """ like a comment """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.OneToOneField(CommentBase, related_name='like', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class RecipeLike(models.Model):
    """ like a recipe """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, related_name='like', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class CommentDislike(models.Model):
    """ dislike a comment """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.OneToOneField(CommentBase, related_name='dislike', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class RecipeDislike(models.Model):
    """ dislike a recipe """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, related_name='dislike', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)