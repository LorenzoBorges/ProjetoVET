# Generated by Django 3.0.8 on 2020-07-19 18:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200719_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='especie',
            field=models.CharField(blank=True, max_length=255, verbose_name='Espécie'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='raca',
            field=models.CharField(max_length=255, verbose_name='Raça'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='descricao_da_vacina',
            field=models.TextField(blank=True, verbose_name='Descrição da vacina'),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.CharField(max_length=255)),
                ('data', models.DateField(blank=True)),
                ('descricao_da_consulta', models.TextField(blank=True, verbose_name='Descrição da consulta')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
    ]
