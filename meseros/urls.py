from django.urls import path
from . import views

urlpatterns = [
    path('api/meseros/mayores-25/', views.obtener_meseros_mayores_25, name='meseros_mayores_25'),
]

# meseros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.CrearMesero.as_view(), name='crear_mesero'),
    path('listar/', views.ListarMeseros.as_view(), name='listar_meseros'),
    path('listar/peru/', views.ListarMeserosPeru.as_view(), name='listar_meseros_peru'),
    path('editar/<int:pk>/', views.EditarMesero.as_view(), name='editar_mesero'),
    path('eliminar/<int:pk>/', views.EliminarMesero.as_view(), name='eliminar_mesero'),
    path('detalle/<int:pk>/', views.VerDetalleMesero.as_view(), name='detalle_mesero'),  # Ruta para ver los detalles
]



from django.urls import path
from .views import listar_meseros

urlpatterns = [
    path('api/listar_meseros/', listar_meseros, name='listar_meseros'),  # Ruta para listar meseros
]

