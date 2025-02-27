from rest_framework import serializers
from .models import User, Session, Clothing, Picture

# Serializer pour User
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=2)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'is_active', 'is_staff']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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