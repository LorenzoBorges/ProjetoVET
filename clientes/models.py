from django.db import models
from django.utils import timezone


class Plano(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    dono = models.CharField(max_length=255)
    animal = models.CharField(max_length=255)
    raca = models.CharField(verbose_name='Raça', max_length=255)
    peso = models.CharField(max_length=255, blank=True)
    especie = models.CharField(verbose_name='Espécie', max_length=255, blank=True)
    idade = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    plano = models.ForeignKey(Plano, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.animal

# class Intermediario(models.Model):
#     dono = models.CharField(max_length=255)
#     dupla_vacina = models.ManyToManyField(Cliente, through='Vacina')

#     def __str__(self):
#         return self.dono

class Vacina(models.Model):
    animal = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vacina = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_vacina = models.TextField(verbose_name='Descrição da vacina', blank=True)

    def __str__(self):
        return self.vacina

class Consulta(models.Model):
    animal = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consulta = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_consulta = models.TextField(verbose_name='Descrição da consulta', blank=True)

    def __str__(self):
        return self.consulta

class Cirurgia(models.Model):
    animal = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cirurgia = models.CharField(max_length=255)
    data = models.DateField(blank=True)
    descricao_da_cirurgia = models.TextField(verbose_name='Descrição da cirurgia', blank=True)

    def __str__(self):
        return self.cirurgia