from django.contrib import admin
from django.urls import path
from freepapp.views import create_article


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/create_article/", create_article, name="create_article"),
]

