# Generated by Django 4.1.3 on 2022-11-29 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopApp', '0012_alter_cliente_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguimiento_id', models.CharField(max_length=70)),
                ('pago', models.IntegerField(choices=[[0, 'reservado'], [1, 'pagado'], [2, 'pendiente de pago']])),
                ('estado', models.IntegerField(choices=[[0, 'servicio realizado'], [1, 'servicio pendiente']])),
                ('barba_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopApp.barba')),
                ('corte_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopApp.cortes')),
                ('estetica_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopApp.estética')),
                ('peinado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopApp.peinado')),
                ('tinte_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopApp.tinte')),
            ],
        ),
    ]
