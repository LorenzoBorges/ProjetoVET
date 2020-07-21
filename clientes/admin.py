from django.contrib import admin
from . import models

class VacinaInline(admin.TabularInline):
    model = models.Vacina
    extra = 1

class ConsultaInline(admin.TabularInline):
    model = models.Consulta
    extra = 1

class CirurgiaInline(admin.TabularInline):
    model = models.Cirurgia
    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'raca', 'dono',
                    'telefone', 'plano', 'mostrar')
    list_display_links = ('id', 'animal', 'dono')
    list_per_page = 10
    search_fields = ('dono', 'animal')
    list_editable = ('telefone', 'mostrar')
    inlines = [
        VacinaInline,
        ConsultaInline,
        CirurgiaInline,
    ]


admin.site.register(models.Plano)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Vacina)
admin.site.register(models.Consulta)
admin.site.register(models.Cirurgia)