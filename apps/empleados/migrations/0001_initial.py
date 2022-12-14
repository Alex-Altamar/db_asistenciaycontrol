# Generated by Django 4.1.2 on 2022-10-06 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('salario', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_llegada', models.DateTimeField()),
                ('h_salida', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado_id', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=75)),
                ('apellidos', models.CharField(max_length=75)),
                ('direccion', models.CharField(max_length=20)),
                ('f_nacimiento', models.DateField()),
                ('foto', models.CharField(max_length=200)),
                ('f_creacion', models.DateField()),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.cargo')),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.horario')),
            ],
        ),
    ]
