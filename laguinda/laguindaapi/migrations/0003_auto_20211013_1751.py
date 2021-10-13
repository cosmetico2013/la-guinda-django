# Generated by Django 3.0.7 on 2021-10-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laguindaapi', '0002_auto_20211011_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='cantidad',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FilePathField(path='imagenes/'),
        ),
    ]