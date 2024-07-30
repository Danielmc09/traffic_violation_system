from django.urls import path
from .views import CargarInfraccionView, GenerarInformeView

urlpatterns = [
    path('cargar_infraccion/', CargarInfraccionView.as_view(), name='cargar_infraccion'),
    path('generar_informe/<str:email>/', GenerarInformeView.as_view(), name='generar_informe'),
]
