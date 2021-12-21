# Generated by Django 4.0 on 2021-12-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('DepCod', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código de departamento')),
                ('DepNom', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
