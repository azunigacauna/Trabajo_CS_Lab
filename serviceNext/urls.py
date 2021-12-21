# from django.urls import include, path
# from publicaciones.views import publicacion_view, FormularioPublicacionView
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("loginCliente", views.loginCliente, name="loginCliente"),
#     path("loginProfesional", views.loginProfesional, name="loginProfesional"),
#     path("perfilUsuario", views.verPerfilUsuario, name="Perfil"),
#     path("perfilProfesional", views.verPerfilProfesional, name="Perfil"),
#     path("loginAdministrador", views.loginAdministrador, name="loginAdministrador"),
#     path("CRUDprofesiones", views.CRUDprofesiones, name="CRUDprofesiones"),
#     path("publicar", publicacion_view, name='publicar'),
#     path("ofertasProfesional",FormularioPublicacionView.listar_Publicaciones, name="ofertasProfesional"),
#     path("responder",views.responderOfertaProfesional, name="responderOfertaProfesional"),
# ]

from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("loginCliente", views.loginCliente, name="loginCliente"),
    path("loginProfesional", views.loginProfesional, name="loginProfesional"),
    path("loginAdministrador", views.loginAdministrador, name="loginAdministrador"),
    path("CRUDprofesiones", views.CRUDprofesiones, name="CRUDprofesiones"),
    path("modificarProfesiones/<id>/",views.modificarProfesiones,name="modificarProfesiones"),
    path("eliminarProfesiones/<id>/",views.eliminarProfesiones,name="eliminarProfesiones"),
    path("agregarProfesiones",views.agregarProfesiones,name="agregarProfesiones"),
    path("publicarTrabajo",views.publicarTrabajo,name="publicarTrabajo"),
    path("registroExitoso",views.registroExitoso,name="registroExitoso"),
    path("modificarTrabajo/<id>/",views.modificarTrabajo,name="modificarTrabajo"),
    path("calificacion", views.calificacion, name="calificacion"),
    path("responderOferta", views.responderOferta, name="responderOferta"),
    path("perfilProfesional", views.perfilProfesional, name="perfilProfesional"),
    path("perfilUsuario", views.perfilUsuario, name="perfilUsuario"),
]