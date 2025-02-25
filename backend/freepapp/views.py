from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
    return HttpResponse("Bienvenue sur l'application Freep !")

# Authentification view    
@api_view(['POST'])
def authenticate_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Check if the user exists
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user) 
        return Response({'message': 'Vous êtes connecté.e'}, status=200)
    else:
        return Response({'error': 'Email ou mot de passe incorrect'}, status=401)

# Get user from session
@api_view(['GET'])
@login_required  # Checks if the user is signed in before answering
def get_user(request):
    user = request.user  
    return Response({'user': {'email': user.email, 'username': user.username}}, status=200)

# Logout user
@api_view(['POST'])
def logout_user(request):
    logout(request)  # Django deletes the session automatically
    return Response({'message': 'Vous êtes déconnecté.e'}, status=200)