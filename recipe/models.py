from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(default='example@example.com')
    recipe_name = models.CharField(max_length=50, null=True, default=None)
    recipe_des = models.TextField()
    recipe_image = models.ImageField(upload_to='media', null=True)
    recipe_count = models.IntegerField(default=1)

    def __str__(self):
        return self.recipe_name


