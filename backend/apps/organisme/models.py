from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.reseaux.models import Reseau


class Adresse(models.Model):
    rue: models.CharField = models.CharField(
        max_length=255,
        verbose_name=_("Rue"),
    )

    code_postal: models.CharField = models.CharField(
        max_length=10,
        verbose_name=_("Code postal"),
    )

    ville: models.CharField = models.CharField(
        max_length=150,
        verbose_name=_("Ville"),
    )

    class Meta:
        verbose_name = _("Adresse")
        verbose_name_plural = _("Adresses")

    def __str__(self) -> str:
        return f"{self.rue}, {self.code_postal} {self.ville}"


class Organisme(models.Model):
    nom: models.CharField = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
    )

    objet: models.CharField = models.CharField(
        max_length=255,
        verbose_name=_("Objet"),
        help_text=_("Objet ou mission principale de l’organisme"),
    )

    description: models.TextField = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    adresse: models.ForeignKey = models.ForeignKey(
        Adresse,
        on_delete=models.PROTECT,
        related_name="organismes",
        verbose_name=_("Adresse"),
    )

    reseau: models.ForeignKey = models.ForeignKey(
        Reseau,
        on_delete=models.PROTECT,
        related_name="organismes",
        verbose_name=_("Reseau"),
    )

    mail: models.EmailField = models.EmailField(
        verbose_name=_("Adresse email"),
    )

    telephone: models.CharField = models.CharField(
        max_length=30,
        verbose_name=_("Téléphone"),
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
        verbose_name = _("Organisme")
        verbose_name_plural = _("Organismes")
        ordering = ["nom"]

    def __str__(self) -> str:
        return self.nom
