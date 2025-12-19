# backend/apps/user/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Militant

User = get_user_model()


@admin.register(Militant)
class MilitantAdmin(admin.ModelAdmin):
    list_display = (
        "prenom",
        "nom",
        "mail",
        "sexe",
        "annee_naissance",
        "a_jour_cotisation",
        "date_creation",
        "date_modification",
    )
    list_filter = ("a_jour_cotisation", "sexe", "annee_naissance")
    search_fields = ("prenom", "nom", "mail")
    ordering = ("nom", "prenom")
    readonly_fields = ("date_creation", "date_modification")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)
