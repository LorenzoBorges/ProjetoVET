from django.shortcuts import render, get_object_or_404
from .models import Cliente, Vacina


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', {
        'clientes': clientes
    })


def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/ver_cliente.html', {
        'cliente': cliente
    })


def lista_vacina(request):
    vacinas = Cliente.objects.all()
    return render(request, 'clientes/vacinas.html', {
        'vacinas': vacinas
    })
