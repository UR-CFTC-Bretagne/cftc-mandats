# backend/apps/user/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Militant

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Administration du modèle User
    """

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Informations personnelles"),
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Dates importantes"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(Militant)
class MilitantAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "prenom",
        "user",
        "mail",
        "a_jour_cotisation",
        "sexe",
        "annee_naissance",
    )
    list_filter = (
        "a_jour_cotisation",
        "sexe",
    )
    search_fields = (
        "nom",
        "prenom",
        "mail",
        "user__username",
        "user__email",
    )
    ordering = ("nom", "prenom")
