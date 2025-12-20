from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.organisme.models import Adresse


class Mandataire(models.Model):
    class Structure(models.TextChoices):
        UL = "UL", _("Union Locale (UL)")
        UD = "UD", _("Union Départementale (UD)")
        UR = "UR", _("Union Régionale (UR)")
        FEDERATION = "FEDERATION", _("Fédération")
        CONFEDERATION = "CONFEDERATION", _("Confédération")
        SYNDICAT = "SYNDICAT", _("Syndicat")

    nom: models.CharField = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
        help_text=_("Nom du mandataire ou de la structure"),
    )

    structure: models.CharField = models.CharField(
        max_length=20,
        choices=Structure.choices,
        verbose_name=_("Structure"),
    )

    adresse: models.ForeignKey = models.ForeignKey(
        Adresse,
        on_delete=models.PROTECT,
        related_name="mandataires",
        verbose_name=_("Adresse postale"),
    )

    mail: models.EmailField = models.EmailField(
        verbose_name=_("Adresse email"),
    )

    date_creation: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Créé le"),
    )

    date_modification: models.DateTimeField = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Modifié le"),
    )

    class Meta:
        verbose_name = _("Mandataire")
        verbose_name_plural = _("Mandataires")
        ordering = ["structure", "nom"]
        constraints = [
            models.UniqueConstraint(
                fields=["nom", "structure"],
                name="unique_mandataire_nom_structure",
            )
        ]

    def __str__(self) -> str:
        return f"{self.nom}"
