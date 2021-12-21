from django.urls import path
from . import views

urlpatterns = [
    path("registroCliente", views.registroCliente, name="registroCliente"),
    path("loginCliente", views.loginCliente, name="loginCliente"),
    path("logoutCliente", views.logoutCliente, name="logoutCliente"),
    path("registroProfesional", views.registroProfesional, name="registroProfesional"),
    path("loginProfesional", views.loginProfesional, name="loginProfesional"),
    path("logoutProfesional", views.logoutProfesional, name="logoutProfesional"),
    path("loginAdministrador", views.loginAdministrador, name="loginAdministrador"),
]