from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Mandataire


class MandataireListView(LoginRequiredMixin, ListView):
    model = Mandataire
    template_name = "mandataire_list.html"
    context_object_name = "mandataires"
    paginate_by = 25
    ordering = ["nom"]


class MandataireDetailView(LoginRequiredMixin, DetailView):
    model = Mandataire
    template_name = "mandataire_detail.html"


class MandataireCreateView(LoginRequiredMixin, CreateView):
    model = Mandataire
    fields = "__all__"
    template_name = "mandataire_form.html"
    success_url = reverse_lazy("mandataire:list")


class MandataireUpdateView(LoginRequiredMixin, UpdateView):
    model = Mandataire
    fields = "__all__"
    template_name = "mandataire_form.html"
    success_url = reverse_lazy("mandataire:list")


class MandataireDeleteView(LoginRequiredMixin, DeleteView):
    model = Mandataire
    template_name = "mandataire_confirm_delete.html"
    success_url = reverse_lazy("mandataire:list")
