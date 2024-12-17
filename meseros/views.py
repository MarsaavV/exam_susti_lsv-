
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mesero
from .serializers import MeseroSerializer

@api_view(['GET'])
def obtener_meseros_mayores_25(request):
    meseros = Mesero.objects.filter(edad__gt=25)  # Filtra a los meseros mayores de 25 años
    serializer = MeseroSerializer(meseros, many=True)
    return Response(serializer.data)


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Mesero
from .forms import MeseroForm

# Vista para crear un mesero
class CrearMesero(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/crear_mesero.html'
    success_url = reverse_lazy('listar_meseros')

# Vista para listar meseros de procedencia Perú
class ListarMeserosPeru(ListView):
    model = Mesero
    template_name = 'meseros/listar_meseros_peru.html'
    context_object_name = 'meseros'

    def get_queryset(self):

        return Mesero.objects.filter(procedencia='Perú')


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Mesero
from .forms import MeseroForm

class EditarMesero(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/editar_mesero.html'
    success_url = reverse_lazy('listar_meseros')


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Mesero

class EliminarMesero(DeleteView):
    model = Mesero
    template_name = 'meseros/eliminar_mesero.html'
    success_url = reverse_lazy('listar_meseros')


from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Mesero

class ListarMeseros(ListView):
    model = Mesero
    template_name = 'meseros/listar_meseros.html'
    context_object_name = 'meseros'



# meseros/views.py
from django.views.generic import DetailView
from .models import Mesero

class VerDetalleMesero(DetailView):
    model = Mesero
    template_name = 'meseros/detalle_mesero.html'
    context_object_name = 'mesero'



from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Mesero
from .serializers import MeseroSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Protege la API con JWT
def listar_meseros(request):

    meseros = Mesero.objects.all()  # Obtiene todos los meseros
    serializer = MeseroSerializer(meseros, many=True)  # Serializa los datos
    return Response(serializer.data)  # Retorna los datos en formato JSON
