from django.contrib import admin
from . import models
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class PlanoInline(NestedStackedInline):
    model = models.Plano
    extra = 1
    fk_name='level'

class VacinaInline(NestedStackedInline):
    model = models.Vacina
    extra = 1
    fk_name='level'

class ConsultaInline(NestedStackedInline):
    model = models.Consulta
    extra = 1
    fk_name='level'
    
class CirurgiaInline(NestedStackedInline):
    model = models.Cirurgia
    extra = 1
    fk_name='level'


class AnimalInline(NestedStackedInline):
    model = models.Animal
    extra = 1
    fk_name = 'level'
    inlines = [VacinaInline, CirurgiaInline, ConsultaInline, PlanoInline]

class ClienteAdmin(NestedModelAdmin):
    list_display = ('id', 'cliente',
                    'telefone', 'mostrar')
    list_display_links = ('id', 'cliente')
    list_per_page = 10
    search_fields = ('cliente',)
    list_editable = ('telefone', 'mostrar')
    inlines = [AnimalInline]


admin.site.register(models.Plano)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Consulta)
admin.site.register(models.Cirurgia)
admin.site.register(models.Vacina)