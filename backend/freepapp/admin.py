from django.contrib import admin
from .models import User, Session, Clothing, Picture
# Register your models here.

admin.site.register(User)
admin.site.register(Session)
admin.site.register(Clothing)
admin.site.register(Picture)