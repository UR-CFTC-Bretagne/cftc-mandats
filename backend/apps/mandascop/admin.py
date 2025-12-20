from django.contrib import admin

from .models import Fiche


@admin.register(Fiche)
class FicheAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "organisme",
        "mandataire",
        "duree_mandat",
        "frequence_reunions",
        "maintien_salaire",
        "frais_kms",
        "restauration",
        "hebergement",
        "type_mandat",
        "reseau",
        "date_creation",
    )
    list_filter = (
        "frequence_reunions",
        "maintien_salaire",
        "frais_kms",
        "restauration",
        "hebergement",
        "type_mandat",
        "reseau",
        "date_creation",
    )
    search_fields = (
        "mandataire__nom",
        "mandataire__prenom",
        "organisme__nom",
        "reseau__nom",
    )
    readonly_fields = ("date_creation", "date_modification")
    ordering = ("-date_creation",)
