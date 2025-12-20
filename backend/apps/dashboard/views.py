# dashboard/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.mandat.models import Mandat
from apps.mandataire.models import Mandataire
from apps.user.models import Militant


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Comptages
        context["total_mandats"] = Mandat.objects.count()
        context["total_militants"] = Militant.objects.count()
        context["total_mandataires"] = Mandataire.objects.count()

        # Mandats récents
        context["recent_mandats"] = Mandat.objects.select_related(
            "militant", "organisme"
        ).order_by("-date_creation")[:10]

        return context
