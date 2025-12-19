from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Militant(User):
    SEXE_CHOICES: list[tuple[str, str]] = [
        ("M", "Masculin"),
        ("F", "Féminin"),
    ]

    nom: models.CharField = models.CharField(max_length=150, verbose_name=_("Nom"))
    prenom: models.CharField = models.CharField(
        max_length=150, verbose_name=_("Prénom")
    )
    mail: models.EmailField = models.EmailField(unique=True, verbose_name=_("Email"))
    a_jour_cotisation: models.BooleanField = models.BooleanField(
        default=False, verbose_name=_("À jour de cotisation")
    )
    sexe: models.CharField = models.CharField(
        max_length=1, choices=SEXE_CHOICES, verbose_name=_("Sexe")
    )
    annee_naissance: models.PositiveSmallIntegerField = (
        models.PositiveSmallIntegerField(verbose_name=_("Année de naissance"))
    )

    date_creation: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Créé le")
    )
    date_modification: models.DateTimeField = models.DateTimeField(
        auto_now=True, verbose_name=_("Modifié le")
    )

    class Meta:
        verbose_name = _("Militant")
        verbose_name_plural = _("Militants")
        ordering = ["nom", "prenom"]

    def __str__(self):
        return f"{self.prenom} {self.nom}"
