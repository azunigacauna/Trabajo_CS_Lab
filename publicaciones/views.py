
# # Create your views here.
# from django.shortcuts import redirect, render
# from django.views.generic.edit import FormView
# from django.http import HttpResponse
# from django.views import generic
# from django.views.generic import ListView, View

# from profesiones.models import Profesion
# from .forms import PublicacionForms
# from .models import Publicacion
# from django.http import HttpRequest


# # Create your views here.
# class PublicacionFormView(FormView):
#     form_class = PublicacionForms
#     template_name = "publicar.html"
#     success_url =" "


# def publicacion_view(request):
#     form = PublicacionForms()
#     if request.method == 'POST':
#         form = PublicacionForms(request.POST)
#         if form.is_valid():
#             print("Valido")
#             pub = Publicacion()
#             pub.PubUsuNorCod = form.cleaned_data['PubUsuNorCod']
#             pub.PubProfCod  = form.cleaned_data['PubProfCod']
#             pub.PubDes = form.cleaned_data['PubDes']
#             pub.PubFecIni  = form.cleaned_data['PubFecIni']
#             pub.save()


#         else:
#             print("Invalido")
#     return render(request, 'publicar.html', {'form': form})

# class FormularioPublicacionView(HttpRequest):

#     def listar_Publicaciones(request):
#         publicaciones=Publicacion.objects.all()
#         return render(request,"ofertasProfesional.html",{"publicaciones":publicaciones})
from django.shortcuts import render
from .models import Publicacion
from django.contrib.auth.models import User, auth
from django.db.models import Q

def publicaciones(request):
    busqueda = request.GET.get("buscar")
    publicaciones = Publicacion.objects.all()
    profesionales = User.objects.all()
    if busqueda:
       publicaciones = Publicacion.objects.filter(
           Q(Distrito__icontains= busqueda) |
           Q(EstadoTrabajo__icontains = busqueda) |
           Q(Correo__icontains = busqueda) 
       ).distinct()
    return render(request, "publicaciones.html", {'publicaciones' : publicaciones, 'profesionales' : profesionales})

# Ver publicaciones de ofertas por parte del Profesional
def verPropuestas(request):
    busqueda = request.GET.get("buscar")
    publicaciones = Publicacion.objects.all()
    profesionales = User.objects.all()
    if busqueda:
       publicaciones = Publicacion.objects.filter(
           Q(Distrito__icontains= busqueda) |
           Q(EstadoTrabajo__icontains = busqueda) |
           Q(Correo__icontains = busqueda) 
       ).distinct()
    return render(request, "ofertasProfesional.html", {'publicaciones' : publicaciones, 'profesionales' : profesionales})

# Responder oferta de trabajo
def responderOferta(request):
    return render(request, "responder.html")