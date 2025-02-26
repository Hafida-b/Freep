from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


# Gestionnaire pour User
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir une adresse email")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hachage du mot de passe
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # S'assurer que is_staff est True
        extra_fields.setdefault("is_superuser", True)  # S'assurer que is_superuser est True

        # La condition suivante garantit que l'utilisateur superuser aura un mot de passe haché
        if password is None:
            raise ValueError("Le mot de passe ne peut pas être vide pour un super utilisateur")

        return self.create_user(email, password, **extra_fields)


# Modèle User
class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    
    # Champs Django obligatoires
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        """Retourne True si l'utilisateur a une permission spécifique."""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Retourne True si l'utilisateur a les permissions pour voir l'application `app_label`."""
        return self.is_superuser

    def __str__(self):
        return self.email if self.email else "Utilisateur sans email"

# Modèle Session
class Session(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")

    def __str__(self):
        return f"Session {self.session_id} de {self.user.email}"

# Modèle Clothing
class Clothing(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    genders = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dressing", blank=True, null=True)

    def __str__(self):
        return self.name if self.name else f"Vêtement #{self.id}"

# Modèle Picture
class Picture(models.Model):
    url = models.URLField(blank=True, null=True)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, related_name="pictures", blank=True, null=True)

    def __str__(self):
        return self.url if self.url else f"Image #{self.id}"