from rest_framework import serializers
from .models import User, Session, Clothing, Picture

# Serializer pour User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'is_active', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}  # Ne pas exposer le mot de passe

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', '')
        )
        return user


# Serializer pour Session
class SessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Inclure les infos utilisateur

    class Meta:
        model = Session
        fields = ['id', 'session_id', 'user']


# Serializer pour Clothing
class ClothingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Ne pas modifier l'utilisateur directement

    class Meta:
        model = Clothing
        fields = ['id', 'name', 'description', 'type', 'size', 'genders', 'state', 'user']


# Serializer pour Picture
class PictureSerializer(serializers.ModelSerializer):
    clothing = ClothingSerializer(read_only=True)  # Associer la photo au vêtement

    class Meta:
        model = Picture
        fields = ['id', 'url', 'clothing']