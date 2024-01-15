from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Pokedex



@register(Pokedex)
class PokedexIndex(AlgoliaIndex):
    fields = [
        'pokedex_num',
        'name',
        'description',
        'abilities',
        'types',
        'location',
        'total_locations',
        'base_stats',
    ]
    settings = {
        'searchableAttributes': ['pokedex_num', 'name', 'abilities', 'types']
    }



# Notes

# Use: python manage.py algolia_reindex
# In order to register the models after creating an index
