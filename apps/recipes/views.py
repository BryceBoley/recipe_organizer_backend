from rest_framework import generics
from serializers import *


class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class AddRecipe(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientsList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


def submit(request):
    recipes = Recipe.objects.all().sort_by('name')
    if request.method == "POST":
        print request.POST['recipe']
        print request.POST['ingredient']

    return render(request, '/add-recipe.html', {})
