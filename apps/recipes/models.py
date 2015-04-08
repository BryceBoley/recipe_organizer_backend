from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, help_text="This is a quick description of your recipe")
    directions = models.TextField(blank=True, help_text="How to make the recipe")
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name
