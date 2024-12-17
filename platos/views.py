# platos/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Plato
from .serializers import PlatoSerializer
from rest_framework.views import APIView


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_platos(request):
    """
    API para listar todos los platos.
    Solo accesible por usuarios autenticados.
    """
    platos = Plato.objects.all()  # Obtiene todos los platos
    serializer = PlatoSerializer(platos, many=True)  # Serializa los datos
    return Response(serializer.data)  # Devuelve los datos en formato JSON


class PlatosMenores40Peru(APIView):
    permission_classes = [IsAuthenticated]  # Protege la vista con autenticación

    def get(self, request):

        platos = Plato.objects.filter(precio__lt=40, procedencia="Perú")
        serializer = PlatoSerializer(platos, many=True)
        return Response(serializer.data)

class PlatosEspanaColombia(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        platos = Plato.objects.filter(procedencia__in=["España", "Colombia"])
        serializer = PlatoSerializer(platos, many=True)
        return Response(serializer.data)