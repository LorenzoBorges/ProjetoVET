# Generated by Django 3.0.8 on 2020-07-29 07:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_cirurgia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='animal',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='plano',
            old_name='nome',
            new_name='plano',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='dono',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='plano',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='raca',
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_registro',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de registro'),
        ),
        migrations.AlterField(
            model_name='cirurgia',
            name='animal',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='animal',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='animal',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=255)),
                ('raca', models.CharField(max_length=255, verbose_name='Raça')),
                ('peso', models.CharField(blank=True, max_length=255)),
                ('especie', models.CharField(blank=True, max_length=255, verbose_name='Espécie')),
                ('idade', models.CharField(blank=True, max_length=255)),
                ('cliente', models.CharField(max_length=255, null=True)),
                ('mostrar', models.BooleanField(default=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cirurgia',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AddField(
            model_name='plano',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
        migrations.AddField(
            model_name='vacina',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Animal'),
        ),
    ]