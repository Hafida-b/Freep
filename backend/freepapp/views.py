from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Clothing, Picture, Session
from .serializers import ClothingSerializer

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