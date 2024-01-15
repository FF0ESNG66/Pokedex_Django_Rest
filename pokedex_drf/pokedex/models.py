from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError



class Pokedex(models.Model):

    class PokemonTypes(models.TextChoices):
            NORMAL = 'Normal', 'Normal'
            FIRE = 'Fire', 'Fire'
            WATER = 'Water', 'Water'
            GRASS = 'Grass', 'Grass'
            ELECTRIC = 'Electric', 'Electric'
            ICE = 'Ice', 'Ice'
            FIGHTING = 'Fighting', 'Fighting'
            POISON = 'Poison', 'Poison'
            GROUND = 'Ground', 'Ground'
            FLYING = 'Flying', 'Flying'
            PSYCHIC = 'Psychic', 'Psychic'
            BUG = 'Bug', 'Bug'
            ROCK = 'Rock', 'Rock'
            GHOST = 'Ghost', 'Ghost'
            DRAGON = 'Dragon', 'Dragon'
            DARK = 'Dark', 'Dark'
            STEEL = 'Steel', 'Steel'

    pokedex_num = models.SmallIntegerField(blank=False, null=False, unique=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    description = models.CharField(max_length=250, blank=False, null=False, unique=True)
    abilities = ArrayField(
        models.CharField(max_length=30, blank=False, null=False),
        size=8,
        blank=False,
        null=False
    )
    types = ArrayField(
        models.CharField(max_length=8, null=False, blank=False, choices=PokemonTypes.choices),
        size=2,
        blank=False,
        null=False
    )
    location = ArrayField(
        models.CharField(max_length=50, blank=False, null=False),
        size = 70,
        blank=False,
        null=False
    )
    base_stats = JSONField()


    class Meta:
        verbose_name = "pokedex"
        verbose_name_plural = "pokedexes"
        db_table = "pokedex"


    def __str__(self) -> str:
        return self.name
    

    def clean(self):
        for value in self.base_stats.values():
            if not isinstance(value, int) or value < 0:
                raise ValidationError('All values must be integers and non-negative integers.')
        self.normalize_types()
        super().clean()
    
    
    @property
    def total_locations(self) -> int:
        return len(self.location)
    
    