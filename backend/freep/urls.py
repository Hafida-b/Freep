from django.contrib import admin
from django.urls import path
from freepapp.views import create_article, delete_article, update_article



from freepapp.views import (
    UserListCreateView, UserDetailView,
    SessionListCreateView, SessionDetailView,
    ClothingListCreateView, ClothingDetailView,
    PictureListCreateView, PictureDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/create_article/", create_article, name="create_article"),
    path('api/delete_article/<int:article_id>/', delete_article, name='delete_article'),
    path('api/update_article/<int:article_id>/', update_article, name='update_article'),
    # path('', views.index, name='index'),
    # Routes pour User
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Routes pour Session
    path('sessions/', SessionListCreateView.as_view(), name='session-list-create'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session-detail'),

    # Routes pour Clothing
    path('clothing/', ClothingListCreateView.as_view(), name='clothing-list-create'),
    path('clothing/<int:pk>/', ClothingDetailView.as_view(), name='clothing-detail'),

    # Routes pour Picture
    path('pictures/', PictureListCreateView.as_view(), name='picture-list-create'),
    path('pictures/<int:pk>/', PictureDetailView.as_view(), name='picture-detail'),
]
