from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cliente_id>', views.ver_cliente, name='ver_cliente'),
]
