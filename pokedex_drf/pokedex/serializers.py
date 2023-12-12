from rest_framework import serializers
from .models import Pokedex
from api.validators import unique_field, int_unique_field


class PokedexSerializer(serializers.ModelSerializer):
    pokedex_num = serializers.IntegerField(validators=[int_unique_field])
    name = serializers.CharField(validators=[unique_field])
    description = serializers.CharField(validators=[unique_field])
    
    class Meta:
        model = Pokedex
        fields = [
            'pokedex_num',
            'name',
            'description',
            'abilities',
            'types',
            'location',
            'total_locations',
            'base_stats'
        ]


    def create(self, validated_data):
        self.capitalize_data(validated_data)
        return super().create(validated_data)

    
    def capitalize_data(self, data):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.capitalize()  
            elif isinstance(value, list):
                data[key] = [item.capitalize() for item in value if isinstance(item, str)]



class PokedexUpdateSerializer(serializers.ModelSerializer):
    pokedex_num = serializers.IntegerField(required=False, validators=[int_unique_field])
    name = serializers.CharField(required=False, validators=[unique_field])
    description = serializers.CharField(required=False, validators=[unique_field])
    abilities = serializers.ListField(required=False)
    types = serializers.ListField(required=False)
    location = serializers.ListField(required=False)
    base_stats = serializers.JSONField(required=False)
    
    class Meta:
        model = Pokedex
        fields = [
            'pokedex_num',
            'name',
            'description',
            'abilities',
            'types',
            'location',
            'total_locations',
            'base_stats'
        ]

    def validate(self, attrs):
        for field in self.fields:
            if field in attrs and attrs[field] == '':
                attrs.pop(field)
        return attrs


    def update(self, instance, validated_data):
        self.capitalize_data(validated_data)
        return super().update(instance, validated_data)
    

    def capitalize_data(self, data):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.capitalize()  
            elif isinstance(value, list):
                data[key] = [item.capitalize() for item in value if isinstance(item, str)]




# Current point

# ProgrammingError at /api/pokedex/update/Test/

# function upper(integer) does not exist
# LINE 1: ...ex" WHERE (UPPER("pokedex"."pokedex_num"::text) = UPPER(1231...

# ^ That's the error