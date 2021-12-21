from django.forms import *
from django import forms
from .models import Publicacion

# class PublicacionForms(forms.ModelForm):
#     class Meta:
#         model = Publicacion
#         fields = ['PubUsuNorCod', 'PubProfCod', 'PubDes', 'PubFecIni']
#         labels = {
#             'PubUsuNorCod': 'Usuario',
#             'PubProfCod': 'Profesional',
#             'PubDes': 'Descripcion', 
#             'PubFecIni': 'Fecha'
#         }
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['Nombres', 'Apellidos', 'Correo','Distrito', 'Descripcion', 'Celular', 'EstadoTrabajo']

        widgets = {
            'Nombres' :TextInput(
                attrs={
                    'required': True,
                }
            ),
            'Apellidos' :TextInput(
                attrs={
                    'required': True,
                }
            ),
            'Correo' :EmailInput(
                attrs={
                    'required': True,
                }
            ),
            'Distrito' :Select(
                attrs={
                    'required': True
                }
            ),
            'Descripcion' :Textarea(
                attrs={
                    'required': True,
                }
            ),
            'Celular' :NumberInput(
                attrs={
                    'required': True,
                }
            ),
            'EstadoTrabajo' :Select(
                attrs={
                    'required': True,
                }
            ),
        }