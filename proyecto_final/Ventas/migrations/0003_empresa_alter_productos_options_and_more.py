# Generated by Django 4.1.1 on 2022-09-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Empresa')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefonos', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logos/')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ('nombre',),
            },
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['nombre'], 'verbose_name': 'Profesores', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='foto',
        ),
    ]
