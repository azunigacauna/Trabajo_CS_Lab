from django.urls import path, include
from . import views

urlpatterns = [
    path("publicaciones", views.publicaciones, name="publicaciones"),
    path("verPropuestas", views.verPropuestas, name="verPropuestas"),
    path("responderOferta", views.responderOferta, name="responderOferta"),
    path('accounts/', include('accounts.urls')),
]