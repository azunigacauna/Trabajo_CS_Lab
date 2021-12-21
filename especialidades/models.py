from django.db import models
from profesiones.models import Profesion

# Create your models here.
class Especialidad(models.Model):
    EspCod		= models.CharField(verbose_name='Código de la especialidad', max_length=10, primary_key=True)
    EspDes		= models.CharField(verbose_name='Descripción', max_length=100, blank=True, null=True)
    EspProCod	= models.ForeignKey(Profesion, verbose_name='Profesion', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.EspDes

    def get_absolute_url(self):
        return reverse('Editar_Especialidad',kwargs={'pk': self.EspCod})