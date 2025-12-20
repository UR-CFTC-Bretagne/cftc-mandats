from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.mandascop.models import Fiche
from apps.mandataire.models import Mandataire
from apps.organisme.models import Organisme
from apps.reseaux.models import Reseau
from apps.user.models import Militant


class Mandat(models.Model):
    TYPE_CHOICES = [
        ("titulaire", "Titulaire"),
        ("suppleant", "Suppléant"),
    ]

    militant: Militant = models.ForeignKey(
        Militant,
        on_delete=models.PROTECT,
        related_name="mandats",
        verbose_name=_("Militant"),
    )
    organisme: Organisme = models.ForeignKey(
        Organisme,
        on_delete=models.PROTECT,
        related_name="mandats",
        verbose_name=_("Organisme"),
    )
    type_mandat: models.CharField = models.CharField(
        max_length=10, choices=TYPE_CHOICES, verbose_name=_("Type")
    )

    # Nouveaux champs
    reseau: Reseau = models.ForeignKey(
        Reseau,
        on_delete=models.PROTECT,
        related_name="mandats",
        verbose_name=_("Réseau"),
    )
    fiche_mandascop: Fiche = models.ForeignKey(
        Fiche,
        on_delete=models.PROTECT,
        related_name="mandats",
        verbose_name=_("Fiche Mandascop"),
    )
    mandataire: Mandataire = models.ForeignKey(
        Mandataire,
        on_delete=models.PROTECT,
        related_name="mandats",
        verbose_name=_("Mandataire"),
    )

    date_creation: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Créé le")
    )
    date_modification: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name=_("Modifié le")
    )

    class Meta:
        verbose_name = _("Mandat")
        verbose_name_plural = _("Mandats")
        ordering = ["militant", "organisme"]

    def __str__(self):
        return f"{self.militant} - {self.organisme} ({self.type_mandat})"
