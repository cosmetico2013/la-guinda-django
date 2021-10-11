# Generated by Django 3.0.7 on 2021-10-11 16:46

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('laguindaapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Valoracione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.DecimalField(decimal_places=0, max_digits=5)),
                ('comentario', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Ingredientes',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nomproduc',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='apeusu',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='correousu',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nomusu',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='idProduc',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='idusu',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valoracione',
            name='valoproduc',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='laguindaapi.Producto'),
        ),
        migrations.AddField(
            model_name='valoracione',
            name='valousu',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='laguindaapi.Usuario'),
        ),
        migrations.AddField(
            model_name='componente',
            name='compoingre',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='laguindaapi.Ingrediente'),
        ),
        migrations.AddField(
            model_name='componente',
            name='compoprodu',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='laguindaapi.Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to='laguindaapi.Oferta'),
        ),
    ]