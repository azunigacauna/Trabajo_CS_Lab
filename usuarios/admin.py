from django.contrib import admin
from .models import UsuarioProfesional, UsuarioNormal

# Register your models here.
admin.site.register(UsuarioProfesional)
admin.site.register(UsuarioNormal)