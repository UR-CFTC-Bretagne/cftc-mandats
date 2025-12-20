from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Militant(models.Model):
    SEXE_CHOICES = [
        ("M", _("Masculin")),
        ("F", _("Féminin")),
    ]

    user: models.OneToOneField = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="militant",
        verbose_name=_("Utilisateur"),
    )

    nom: models.CharField = models.CharField(
        max_length=150,
        verbose_name=_("Nom"),
    )

    prenom: models.CharField = models.CharField(
        max_length=150,
        verbose_name=_("Prénom"),
    )

    mail: models.EmailField = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
    )

    a_jour_cotisation: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name=_("À jour de cotisation"),
    )

    sexe: models.CharField = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES,
        verbose_name=_("Sexe"),
    )

    annee_naissance: models.PositiveSmallIntegerField = (
        models.PositiveSmallIntegerField(
            verbose_name=_("Année de naissance"),
        )
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
        verbose_name = _("Militant")
        verbose_name_plural = _("Militants")
        ordering = ["nom", "prenom"]

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"
