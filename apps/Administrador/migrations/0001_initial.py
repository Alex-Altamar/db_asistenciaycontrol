# Generated by Django 4.1.2 on 2022-10-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('contraseña', models.CharField(max_length=60)),
                ('nombres', models.CharField(max_length=75)),
                ('apellidos', models.CharField(max_length=75)),
                ('foto', models.CharField(max_length=200)),
                ('f_creacion', models.DateField()),
            ],
        ),
    ]
