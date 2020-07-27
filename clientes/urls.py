from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vacinas/', views.lista_vacina, name='lista_vacina'),
    path('<int:cliente_id>', views.ver_cliente, name='ver_cliente'),
]
