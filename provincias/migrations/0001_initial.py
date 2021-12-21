# Generated by Django 4.0 on 2021-12-09 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('ProvCod', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Código de provincia')),
                ('ProvNom', models.CharField(max_length=50, verbose_name='Nombre de la provincia')),
                ('ProvDepCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name_plural': 'Provincias',
                'unique_together': {('ProvDepCod', 'ProvCod')},
            },
        ),
    ]
