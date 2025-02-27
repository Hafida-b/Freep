from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import User, Clothing, Picture, Session
from .serializers import UserSerializer, SessionSerializer, ClothingSerializer, PictureSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import Clothing
from .serializers import ClothingSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_article(request):
    """
    API pour créer un article (vêtement)
    """
    # session_id = request.COOKIES.get("auth_user_session_id")

    # if not session_id:
    #     return Response({"message": "Utilisateur non authentifié"}, status=status.HTTP_401_UNAUTHORIZED)

    # Vérifier si la session existe
    # session = get_object_or_404(Session, session_id=session_id)
    
    # Extraire les données envoyées
    data = request.data
    name = data.get("name")
    desc = data.get("desc")
    type_ = data.get("type")
    size = data.get("size")
    gender = data.get("gender")
    state = data.get("state")
    image_url = data.get("image")

    # Créer un nouvel article
    clothing = Clothing.objects.create(
        name=name,
        description=desc,
        type=type_,
        size=size,
        genders=gender,
        state=state,
        # user=session.user  # Associer l'article à l'utilisateur de la session
    )

    # Ajouter l'image associée
    if image_url:
        Picture.objects.create(clothing=clothing, url=image_url)

    return Response({"message": "Article créé avec succès"}, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_article(request, article_id):
    """
    API pour supprimer un article (vêtement) à partir de son ID.
    """
    try:
        # Récupérer l'article via l'ID
        clothing = Clothing.objects.get(id=article_id)

        # Supprimer l'article
        clothing.delete()

        return Response({"message": "Article supprimé avec succès"}, status=200)

    except Clothing.DoesNotExist:
        return Response({"message": "Article non trouvé"}, status=404)


@api_view(["PUT"])  # On utilise PUT pour la mise à jour
def update_article(request, article_id):
    """
    API pour mettre à jour un article (vêtement) à partir de son ID.
    """
    # Essayer de récupérer l'article avec l'ID donné
    try:
        clothing = Clothing.objects.get(id=article_id)
    except Clothing.DoesNotExist:
        return Response({"message": "Article non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    # Extraire les données envoyées dans la requête
    data = request.data
    name = data.get("name", clothing.name)  # Si la donnée n'est pas présente, on garde l'ancienne
    desc = data.get("desc", clothing.description)
    type_ = data.get("type", clothing.type)
    size = data.get("size", clothing.size)
    gender = data.get("gender", clothing.genders)
    state = data.get("state", clothing.state)
    image_url = data.get("image", None)

    # Mettre à jour l'article avec les nouvelles données
    clothing.name = name
    clothing.description = desc
    clothing.type = type_
    clothing.size = size
    clothing.genders = gender
    clothing.state = state

    # Sauvegarder les changements
    clothing.save()

    # Si une nouvelle image est fournie, on la met à jour aussi
    if image_url:
        # Si l'article a déjà une image associée, on peut soit la supprimer soit la mettre à jour
        picture = clothing.pictures.first()  # Prendre la première image liée à l'article
        if picture:
            picture.url = image_url
            picture.save()
        else:
            # Si aucune image n'existe encore, on en crée une nouvelle
            Picture.objects.create(clothing=clothing, url=image_url)

@api_view(["GET"])
def list_articles(request):
    """
    API pour récupérer la liste des articles
    """
    articles = Clothing.objects.all()
    serializer = ClothingSerializer(articles, many=True)
    print("data :", serializer.data)
    return Response({"clothingList": serializer.data}, status=status.HTTP_200_OK)

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
    return Response({'user': {'email': user.email, 'username': user.full_name}}, status=200)

# Logout user
@api_view(['POST'])
def logout_user(request):
    return Response({'message': 'Déconnexion réussie'}, status=200)

# Vues pour User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vues pour Session
class SessionListCreateView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# Vues pour Clothing
class ClothingListCreateView(generics.ListCreateAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

class ClothingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

# Vues pour Picture
class PictureListCreateView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class ClothingListCreateView(generics.ListCreateAPIView):
   
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
