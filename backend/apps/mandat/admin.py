from django.contrib import admin

from .models import Mandat


@admin.register(Mandat)
class MandatAdmin(admin.ModelAdmin):
    list_display = (
        "militant",
        "organisme",
        "type_mandat",
        "mandataire",
        "reseau",
        "fiche_mandascop",
        "date_creation",
    )

    list_filter = (
        "type_mandat",
        "reseau",
        "organisme",
        "mandataire",
    )

    search_fields = (
        "militant__nom",
        "militant__prenom",
        "organisme__nom",
        "mandataire__nom",
        "reseau__nom",
    )

    ordering = ("-date_creation",)
