from django.db import models
from django.utils.translation import gettext_lazy as _


class Reseau(models.Model):
    nom: models.CharField = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Nom"),
        help_text=_(
            "Exemples : Santé au travail, Handicap, Sécurité Sociale, Emploi Formation"
        ),
    )
    description: models.TextField = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )
    date_creation: models.DateField = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Créé le"),
    )
    date_modification: models.DateField = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Modifié le"),
    )

    class Meta:
        verbose_name = _("Réseau")
        verbose_name_plural = _("Réseaux")
        ordering = ["nom"]

    def __str__(self) -> str:
        return self.nom
