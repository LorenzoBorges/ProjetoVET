from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Cliente, Vacina
from django.core.paginator import Paginator


def index(request):
    clientes = Cliente.objects.order_by('animal').filter(
        mostrar = True
    )
    paginator = Paginator(clientes, 20)
    page = request.GET.get('p')
    clientes = paginator.get_page(page)
    return render(request, 'clientes/index.html', {
        'clientes': clientes
    })


def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'clientes/ver_cliente.html', {
        'cliente': cliente
    })


# def lista_vacina(request):
#    vacinas = Cliente.objects.all()
#    return render(request, 'clientes/vacinas.html', {
#        'vacinas': vacinas
#    })