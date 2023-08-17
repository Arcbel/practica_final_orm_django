# Generated by Django 4.2.4 on 2023-08-17 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_laboratorio', models.CharField(max_length=40)),
                ('ciudad', models.CharField(default='', max_length=40)),
                ('pais', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('f_fabricacion', models.DateField()),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_director_general', models.CharField(max_length=40)),
                ('especialidad', models.CharField(default='', max_length=40)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
    ]