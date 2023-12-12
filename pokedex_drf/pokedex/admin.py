from django.contrib import admin
from .models import Pokedex



@admin.register(Pokedex)
class CustomPokedexAdmin(admin.ModelAdmin):
    list_display = ['pokedex_num', 'name', 'description', 'abilities', 'types', 'location', 'base_stats']
    search_fields = ['pokedex_num', 'name']
    list_filter = ['types', 'location']