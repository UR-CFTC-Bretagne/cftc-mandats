from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Récupère le modèle User personnalisé ou le modèle standard
User = get_user_model()


# Optionnel : personnalisation du UserAdmin
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("date_joined",)


# Enregistrement dans l’admin
admin.site.register(User, UserAdmin)
