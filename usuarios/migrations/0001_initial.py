# Generated by Django 4.0 on 2021-12-09 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provincias', '0001_initial'),
        ('departamentos', '0001_initial'),
        ('profesiones', '0001_initial'),
        ('distritos', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioProfesional',
            fields=[
                ('UsuProNomUsu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='Nombre de usuario')),
                ('UsuProDNI', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='DNI')),
                ('UsuProRUC', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='RUC')),
                ('UsuProSex', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=1, null=True, verbose_name='Sexo del usuario profesional')),
                ('UsuProFecNac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('UsuProTel1', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de contacto 1')),
                ('UsuProTel2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de contacto 2')),
                ('UsuProCal', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Calificación')),
                ('UsuProVer', models.BooleanField(default=False, verbose_name='Está verificado')),
                ('UsuProDepCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento', verbose_name='Departamento')),
                ('UsuProDisCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distritos.distrito', verbose_name='Distrito')),
                ('UsuProProCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesiones.profesion', verbose_name='Profesión')),
                ('UsuProProvCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provincias.provincia', verbose_name='Provincia')),
            ],
            options={
                'verbose_name_plural': 'Profesionales',
            },
        ),
        migrations.CreateModel(
            name='UsuarioNormal',
            fields=[
                ('UsuNorNomUsu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='Nombre de usuario')),
                ('UsuNorDNI', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='DNI')),
                ('UsuNorSex', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=1, null=True, verbose_name='Sexo del usuario normal')),
                ('UsuNorFecNac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('UsuNorTel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de contacto')),
                ('UsuNorDepCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento', verbose_name='Departamento')),
                ('UsuNorDisCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distritos.distrito', verbose_name='Distrito')),
                ('UsuNorProvCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provincias.provincia', verbose_name='Provincia')),
            ],
            options={
                'verbose_name_plural': 'Usuarios normales',
            },
        ),
    ]