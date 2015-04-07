from django.conf.urls import patterns, url
from recipe_organizer.settings import MEDIA_ROOT
from views import *

urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^add-recipe$', AddRecipe.as_view(), name='add-recipe'),

    url(r'^ingredients/$', IngredientsList.as_view(), name='ingredients-list'),
    # Handling media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
