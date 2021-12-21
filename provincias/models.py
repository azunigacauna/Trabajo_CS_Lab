from django.db import models
from departamentos.models import Departamento

# Create your models here.
class Provincia(models.Model):
    ProvCod		= models.CharField(verbose_name='Código de provincia', max_length=4, primary_key=True)
    ProvNom	    = models.CharField(verbose_name='Nombre de la provincia', max_length=50)
    ProvDepCod	= models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Provincias"
        unique_together = (('ProvDepCod', 'ProvCod'),)

    def __str__(self):
	    return self.ProvNom