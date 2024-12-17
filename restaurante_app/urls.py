from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Importa las vistas de JWT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meseros/', include('meseros.urls')),  # Incluye las rutas de meseros
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta para obtener tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar tokens
    path('platos/', include('platos.urls')),
]
