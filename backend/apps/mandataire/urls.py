from django.urls import path

from .views import (
    MandataireCreateView,
    MandataireDeleteView,
    MandataireDetailView,
    MandataireListView,
    MandataireUpdateView,
)

app_name = "mandataire"

urlpatterns = [
    path("", MandataireListView.as_view(), name="list"),
    path("creer/", MandataireCreateView.as_view(), name="create"),
    path("<int:pk>/", MandataireDetailView.as_view(), name="detail"),
    path("<int:pk>/modifier/", MandataireUpdateView.as_view(), name="update"),
    path("<int:pk>/supprimer/", MandataireDeleteView.as_view(), name="delete"),
]
