from django.db import models
from usuarios.models import UsuarioNormal
from profesiones.models import Profesion

# Create your models here.
# class Publicacion(models.Model):
#     PubUsuNorCod    = models.ForeignKey(UsuarioNormal, verbose_name='Cliente', on_delete=models.CASCADE)
#     PubProfCod      = models.ForeignKey(Profesion, verbose_name='Especialidad', on_delete=models.CASCADE)
#     PubDes          = models.TextField()
#     PubFecIni       = models.DateField(verbose_name='Fecha de publicación', null=True, blank=True)

#     class Meta:
#         verbose_name_plural = "Publicaciones"

#     def __str__(self):
#         return self.PubUsuNorCod.UsuNorNomUsu.first_name + ' ' + self.PubUsuNorCod.UsuNorNomUsu.last_name + ' (' + self.PubUsuNorCod.UsuNorNomUsu.username + ')'

class Publicacion(models.Model):
    Nombres = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    Correo = models.EmailField(max_length=40)
    distrito_choice = [
        ('Alto Selva Alegre', 'Alto Selva Alegre'),
        ('Arequipa', 'Arequipa'),
        ('Cayma', 'Cayma'),
        ('Cerro Colorado', 'Cerro Colorado'),
        ('Characato', 'Characato'),
        ('Chiguata', 'Chiguata'),
        ('Jacobo Hunter', 'Jacobo Hunter'),
        ('Jose Luis Bustamante Y Rivero', 'Jose Luis Bustamante Y Rivero'),
        ('La Joya', 'La Joya'),
        ('Mariano Melgar', 'Mariano Melgar'),
        ('Miraflores', 'Miraflores'),
        ('Mollebaya', 'Mollebaya'),
        ('Paucarpata', 'Paucarpata'),
        ('Pocsi', 'Pocsi'),
        ('Polobaya', 'Polobaya'),
        ('Quequeña', 'Quequeña'),
        ('Sabandia', 'Sabandia'),
        ('Sachaca', 'Sachaca'),
        ('San Juan De Siguas', 'San Juan De Siguas'),
        ('San Juan De Tarucani', 'San Juan De Tarucani'),
        ('Santa Isabel De Siguas', 'Santa Isabel De Siguas'),
        ('Santa Rita De Sihuas', 'Santa Rita De Sihuas'),
        ('Socabaya', 'Socabaya'),
        ('Tiabaya', 'Tiabaya'),
        ('Uchumayo', 'Uchumayo'),
        ('Vitor', 'Vitor'),
        ('Yanahuara', 'Yanahuara'),
        ('Yarabamba', 'Yarabamba'),
        ('Yura', 'Yura'),

    ]
    Distrito = models.CharField(max_length=90, choices = distrito_choice, default="")
    Descripcion = models.TextField(max_length=2000)
    Celular = models.IntegerField()
    estadoTrabajo_choice = [
        ('Activo', 'Estado Activo'),
        ('En Proceso', 'Estado Ocupado'),
        ('Culminado', 'Estado Terminado'),
    ]
    EstadoTrabajo = models.CharField(max_length=20, choices = estadoTrabajo_choice, default="")