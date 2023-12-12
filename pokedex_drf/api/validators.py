from rest_framework.validators import UniqueValidator
from pokedex.models import Pokedex


unique_field = UniqueValidator(queryset=Pokedex.objects.all(), lookup='iexact')

int_unique_field = UniqueValidator(queryset=Pokedex.objects.all(), lookup='exact')