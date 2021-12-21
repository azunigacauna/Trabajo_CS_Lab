from django.db import models
from django.contrib.auth.models import User
from profesiones.models import Profesion
from departamentos.models import Departamento
from provincias.models import Provincia
from distritos.models import Distrito

# Create your models here.
class UsuarioProfesional(models.Model):
    UsuProNomUsu   = models.OneToOneField(User, verbose_name='Nombre de usuario', primary_key=True, on_delete=models.CASCADE)
    UsuProDNI      = models.CharField(verbose_name='DNI', max_length=20, null=True, blank=True, unique=True)
    UsuProRUC       = models.CharField(verbose_name='RUC', max_length=20, null=True, blank=True, unique=True)

    Masculino = 'M'
    Femenino = 'F'
    Otro = 'O'
    sexo_usuario_profesional = [
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
        (Otro, 'Otro'),
    ]

    DEFAULT_PRO = 'VET'
    DEFAULT_DEP = '04'
    DEFAULT_PROV = '0401'
    DEFAULT_DIS = '040128' 
    UsuProProCod	= models.ForeignKey(Profesion, verbose_name='Profesión', on_delete=models.CASCADE, default=DEFAULT_PRO)
    UsuProDepCod    = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE, default=DEFAULT_DEP)
    UsuProProvCod   = models.ForeignKey(Provincia, verbose_name='Provincia', on_delete=models.CASCADE, default=DEFAULT_PROV)
    UsuProDisCod    = models.ForeignKey(Distrito, verbose_name='Distrito', on_delete=models.CASCADE, default=DEFAULT_DIS)
    UsuProSex       = models.CharField(verbose_name='Sexo del usuario profesional', max_length=1, choices=sexo_usuario_profesional, default=Masculino, null=True, blank=True)
    UsuProFecNac    = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    UsuProTel1      = models.CharField(verbose_name='Teléfono de contacto 1', max_length=15, null=True, blank=True)
    UsuProTel2      = models.CharField(verbose_name='Teléfono de contacto 2', max_length=15, null=True, blank=True)

    UsuProCal       = models.DecimalField(verbose_name='Calificación', max_digits=2, decimal_places=1, default=0)

    # usuario profesional verificado
    UsuProVer       = models.BooleanField(verbose_name='Está verificado', default=False)
    UsuProPun       = models.IntegerField(verbose_name="Puntuacion", default=0)

    # fecha de registro
    #UsuProFecReg = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return self.UsuProNomUsu.first_name + ' ' + self.UsuProNomUsu.last_name


class UsuarioNormal(models.Model):
    UsuNorNomUsu   = models.OneToOneField(User, verbose_name='Nombre de usuario', primary_key=True, on_delete=models.CASCADE)
    UsuNorDNI      = models.CharField(verbose_name='DNI', max_length=20, null=True, blank=True, unique=True)

    Masculino = 'M'
    Femenino = 'F'
    Otro = 'O'
    sexo_usuario_normal = [
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
        (Otro, 'Otro'),
    ]
    

    DEFAULT_DEP = '04'
    DEFAULT_PROV = '0401'
    DEFAULT_DIS = '040128' 
    UsuNorDepCod    = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE, default=DEFAULT_DEP)
    UsuNorProvCod    = models.ForeignKey(Provincia, verbose_name='Provincia', on_delete=models.CASCADE, default=DEFAULT_PROV)
    UsuNorDisCod    = models.ForeignKey(Distrito, verbose_name='Distrito', on_delete=models.CASCADE, default=DEFAULT_DIS)
    UsuNorSex       = models.CharField(verbose_name='Sexo del usuario normal', max_length=1, choices=sexo_usuario_normal, default=Masculino, null=True, blank=True)
    UsuNorFecNac    = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    UsuNorTel      = models.CharField(verbose_name='Teléfono de contacto', max_length=15, null=True, blank=True)

    # fecha de registro
    #UsuProFecReg = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Usuarios normales'

    def __str__(self):
        return self.UsuNorNomUsu.first_name + ' ' + self.UsuNorNomUsu.last_name