from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}} # <- This setting ensures that the password field won't be included in the serialized output


    def create(self, validated_data):
        validated_data['email'] = validated_data.get('email', '').lower()
        user = User.objects.create_user(**validated_data)
        return user