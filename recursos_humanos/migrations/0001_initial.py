# Generated by Django 5.1.7 on 2025-03-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
    ]
