# Generated by Django 3.2 on 2021-12-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesiones', '0002_auto_20211211_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesion',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profesion',
            name='ProCod',
            field=models.CharField(max_length=10, verbose_name='Código de profesión'),
        ),
    ]
