# Generated by Django 4.1.3 on 2022-11-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopApp', '0003_alter_servicios_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicioss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('hora', models.DateTimeField()),
                ('disponible', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='fotos')),
                ('descripcion', models.TextField(max_length=255)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
    ]
