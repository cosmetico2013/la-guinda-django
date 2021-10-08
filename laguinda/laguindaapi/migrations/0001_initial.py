# Generated by Django 3.0.7 on 2021-10-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('idingre', models.AutoField(primary_key=True, serialize=False)),
                ('nomingre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProduc', models.AutoField(primary_key=True, serialize=False)),
                ('nomproduc', models.CharField(max_length=50)),
                ('oferta', models.CharField(max_length=100)),
                ('imagen', models.FilePathField(path='/home/sergio/Escritorio/la-guinda-django/laguinda')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusu', models.AutoField(primary_key=True, serialize=False)),
                ('nomusu', models.CharField(max_length=50)),
                ('apeusu', models.CharField(max_length=100)),
                ('correousu', models.EmailField(max_length=254)),
            ],
        ),
    ]
