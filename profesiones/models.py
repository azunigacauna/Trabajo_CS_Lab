from django.db import models
from django.urls import reverse

# Create your models here.
class Profesion(models.Model):
    ProCod      = models.CharField(verbose_name='Profesión', max_length=10, primary_key=True)
    img         = models.ImageField(verbose_name='Imagen de profesión', upload_to='pics')
    
    class Meta:
        verbose_name_plural = "Profesiones"

    # def __str__(self):
	   #  return self.ProDes

    # def get_absolute_url(self):
	   #  return reverse('Editar_Profesion', kwargs={'pk': self.ProCod})