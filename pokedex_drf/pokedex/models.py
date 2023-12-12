from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField



class Pokedex(models.Model):
    pokedex_num = models.SmallIntegerField(blank=False, null=False, unique=True)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False, unique=True)
    abilities = ArrayField(
        models.CharField(max_length=30, blank=False, null=False),
        size=8,
        blank=False,
        null=False
    )
    types = ArrayField(
        models.CharField(max_length=15, null=False, blank=False),
        size=4,
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
    
    
    @property
    def total_locations(self) -> int:
        return len(self.location)

