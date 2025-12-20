from django.contrib import admin

from .models import Mandataire


@admin.register(Mandataire)
class MandataireAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "structure",
        "mail",
        "date_creation",
        "date_modification",
    )
    search_fields = ("nom", "mail", "structure")
    list_filter = ("structure", "date_creation")
