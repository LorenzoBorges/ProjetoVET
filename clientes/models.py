from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    cliente = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_registro = models.DateTimeField(verbose_name='Data de registro', default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.cliente

class Animal(models.Model):
    animal = models.CharField(max_length=255)
    raca = models.CharField(verbose_name='Raça', max_length=255)
    peso = models.CharField(max_length=255, blank=True)
    especie = models.CharField(verbose_name='Espécie', max_length=255, blank=True)
    idade = models.CharField(max_length=255, blank=True)
    cliente = models.CharField(max_length=255, null=True)
    mostrar = models.BooleanField(default=True)
    level = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.animal

class Vacina(models.Model):
    animal = models.CharField(max_length=255)
    vacina = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_vacina = models.TextField(verbose_name='Descrição da vacina', blank=True)
    level = models.ForeignKey('Animal', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.vacina

class Consulta(models.Model):
    animal = models.CharField(max_length=255)
    consulta = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_consulta = models.TextField(verbose_name='Descrição da consulta', blank=True)
    level = models.ForeignKey('Animal', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.consulta

class Cirurgia(models.Model):
    animal = models.CharField(max_length=255)
    cirurgia = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_cirurgia = models.TextField(verbose_name='Descrição da cirurgia', blank=True)
    level = models.ForeignKey('Animal', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cirurgia

class Plano(models.Model):
    plano = models.CharField(max_length=255)
    level = models.ForeignKey('Animal', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.plano
