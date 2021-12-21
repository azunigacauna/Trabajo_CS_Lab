from django.db import models
from django.urls import reverse

# Create your models here.
class Departamento(models.Model):
    DepCod		= models.CharField(verbose_name='Código de departamento', max_length=2, primary_key=True)
    DepNom	= models.CharField(verbose_name='Nombre', max_length=50)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __str__(self):
	    return self.DepNom