from django.contrib import admin

from apps.organisme.models import Adresse, Organisme, Reseau


@admin.register(Reseau)
class ReseauAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "date_creation",
        "date_modification",
    )

    search_fields = (
        "nom",
        "description",
    )

    ordering = ("nom",)

    readonly_fields = (
        "date_creation",
        "date_modification",
    )


@admin.register(Adresse)
class AdresseAdmin(admin.ModelAdmin):
    list_display = (
        "rue",
        "code_postal",
        "ville",
    )

    search_fields = (
        "rue",
        "code_postal",
        "ville",
    )

    list_filter = (
        "ville",
        "code_postal",
    )

    ordering = (
        "ville",
        "code_postal",
    )


@admin.register(Organisme)
class OrganismeAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "objet",
        "reseau",
        "ville",
        "mail",
        "telephone",
        "date_creation",
    )

    list_filter = (
        "reseau",
        "adresse__ville",
        "date_creation",
    )

    search_fields = (
        "nom",
        "objet",
        "description",
        "mail",
        "telephone",
        "adresse__rue",
        "adresse__ville",
        "reseau__nom",
    )

    ordering = ("nom",)

    readonly_fields = (
        "date_creation",
        "date_modification",
    )

    fieldsets = (
        (
            ("Informations générales"),
            {
                "fields": (
                    "nom",
                    "objet",
                    "description",
                    "reseau",
                )
            },
        ),
        (
            ("Coordonnées"),
            {
                "fields": (
                    "adresse",
                    "mail",
                    "telephone",
                )
            },
        ),
        (
            ("Suivi"),
            {
                "fields": (
                    "date_creation",
                    "date_modification",
                )
            },
        ),
    )

    @admin.display(description=("Ville"))
    def ville(self, obj: Organisme) -> str:
        return obj.adresse.ville
