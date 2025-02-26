from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def index(request):
    return HttpResponse("Bienvenue sur l'application Freep !")

# Create JWT token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),   # Refresh token
        'access': str(refresh.access_token),  # Access token
    }

# Authentification and generation of JWT    
@api_view(['POST'])
def authenticate_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Checks if the user exists
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({'message': 'Connexion réussie', 'tokens': tokens}, status=200)
    else:
        return Response({'error': 'Email ou mot de passe incorrect'}, status=401)

# Get user info from JWT
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # Checks if the user is signed in

def get_user(request):
    user = request.user  
    return Response({'user': {'email': user.email, 'username': user.username}}, status=200)

# Logout user
@api_view(['POST'])
def logout_user(request):
    return Response({'message': 'Déconnexion réussie'}, status=200)