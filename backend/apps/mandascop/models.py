from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.mandataire.models import Mandataire
from apps.organisme.models import Organisme
from apps.reseaux.models import (
    Reseau,  # thématique (Emplois-formation, Santé au travail...)
)


class Fiche(models.Model):
    organisme: models.ForeignKey = models.ForeignKey(
        Organisme,
        on_delete=models.PROTECT,
        related_name="fiches",
        verbose_name=_("Organisme"),
    )

    mandataire: models.ForeignKey = models.ForeignKey(
        Mandataire,
        on_delete=models.PROTECT,
        related_name="fiches",
        verbose_name=_("Mandataire"),
    )

    duree_mandat: models.CharField = models.CharField(
        max_length=50,
        verbose_name=_("Durée du mandat"),
        blank=True,
    )

    frequence_reunions: models.CharField = models.CharField(
        max_length=100,
        verbose_name=_("Fréquence des réunions"),
        blank=True,
    )

    # Prise en charge
    maintien_salaire: models.BooleanField = models.BooleanField(
        default=False, verbose_name=_("Maintien de salaire")
    )
    frais_kms: models.BooleanField = models.BooleanField(
        default=False, verbose_name=_("Frais kilométriques")
    )
    restauration: models.BooleanField = models.BooleanField(
        default=False, verbose_name=_("Frais de restauration")
    )
    hebergement: models.BooleanField = models.BooleanField(
        default=False, verbose_name=_("Hébergement")
    )

    # Missions et activités
    missions_mandataire: models.TextField = models.TextField(
        verbose_name=_("Missions du mandataire"), blank=True
    )
    temps_investi: models.CharField = models.CharField(
        max_length=50, verbose_name=_("Temps investi dans les mandats"), blank=True
    )
    profil_mandataire: models.TextField = models.TextField(
        verbose_name=_("Profil du mandataire"), blank=True
    )
    institutions_env_mandat: models.TextField = models.TextField(
        verbose_name=_("Institutions dans l'environnement du mandat"), blank=True
    )
    type_mandat: models.CharField = models.CharField(
        max_length=50, verbose_name=_("Type de mandat"), blank=True
    )
    principales_activites: models.TextField = models.TextField(
        verbose_name=_("Principales activités du mandataire"), blank=True
    )
    competences: models.TextField = models.TextField(
        verbose_name=_("Compétences"), blank=True
    )

    # Réseau thématique
    reseau: models.ForeignKey = models.ForeignKey(
        Reseau,
        on_delete=models.PROTECT,
        related_name="fiches",
        verbose_name=_("Thématique (Réseau)"),
        blank=True,
        null=True,
    )

    date_creation: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Créé le")
    )
    date_modification: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name=_("Modifié le")
    )

    class Meta:
        verbose_name = _("Fiche Mandascop")
        verbose_name_plural = _("Fiches Mandascop")
        ordering = ["-date_creation"]

    def __str__(self) -> str:
        return f"Fiche {self.mandataire} - {self.organisme}"
