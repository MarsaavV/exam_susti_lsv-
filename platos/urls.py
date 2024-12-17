from django.urls import path
from .views import listar_platos, PlatosMenores40Peru, PlatosEspanaColombia
urlpatterns = [
    path('listar/', listar_platos, name='listar_platos'),
    path('api/platos/menos-40-peru/', PlatosMenores40Peru.as_view(), name='platos_menos_40_peru'),
    path('api/platos/espana-colombia/', PlatosEspanaColombia.as_view(), name='platos_espana_colombia'),
]
