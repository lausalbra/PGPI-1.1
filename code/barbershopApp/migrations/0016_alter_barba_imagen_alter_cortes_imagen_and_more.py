# Generated by Django 4.1.3 on 2022-12-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopApp', '0015_barba_estado_barba_pago_cortes_estado_cortes_pago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barba',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='cortes',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='estética',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='peinado',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='tinte',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
    ]
