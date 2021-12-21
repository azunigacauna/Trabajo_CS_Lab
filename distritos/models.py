from django.db import models
from departamentos.models import Departamento
from provincias.models import Provincia

# Create your models here.
class Distrito(models.Model):
    DisCod		= models.CharField(verbose_name='Código de distrito', max_length=6, primary_key=True)
    DisNom	    = models.CharField(verbose_name='Descripción', max_length=50)
    DisDepCod   = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE)
    DisProvCod	= models.ForeignKey(Provincia, verbose_name='Provincia', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Distritos"
        unique_together = (('DisDepCod','DisProvCod', 'DisCod'),)

    def __str__(self):
	    return self.DisNom