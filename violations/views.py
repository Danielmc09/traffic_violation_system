from rest_framework import status, views
from rest_framework.response import Response
from people.models import Person
from .models import Violation
from .serializers import ViolationSerializer
from vehicles.models import Vehicle
from officers.models import Officer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class CargarInfraccionView(views.APIView):
    """
        Vista API para registrar una infracción de tráfico.

        Methods:
            post(request): Crea una nueva infracción de tráfico.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
            Crea una nueva infracción para un vehículo específico.

            Args:
                request (HttpRequest): La solicitud HTTP que contiene los datos de la infracción.

            Returns:
                JsonResponse: Una respuesta JSON con los detalles de la infracción creada o un mensaje de error.
        """
        data = request.data
        try:
            vehicle = Vehicle.objects.get(license_plate=data['placa_patente'])
        except Vehicle.DoesNotExist:
            return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            officer = Officer.objects.get(user=request.user)
        except Officer.DoesNotExist:
            return Response({'error': 'Officer not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
            current_date = datetime.now()
            if timestamp.date() < current_date.date():
                return Response({'error': 'Violation date cannot be in the past'}, status=status.HTTP_400_BAD_REQUEST)
            if timestamp.date() > current_date.date():
                return Response({'error': 'Violation date cannot be in the future'}, status=status.HTTP_400_BAD_REQUEST)

            violation = Violation.objects.create(
                vehicle=vehicle,
                officer=officer,
                timestamp=timestamp,
                comments=data['comentarios']
            )
            serializer = ViolationSerializer(violation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerarInformeView(views.APIView):
    """
        Vista API para generar un informe de infracciones basado en el correo electrónico de la persona.

        Métodos:
            get(request, email): Devuelve un informe de infracciones.
    """
    permission_classes = []  # Elimina las restricciones de permisos

    def get(self, request, email):
        """
            Genera un informe de infracciones basado en el correo electrónico de la persona.

            Args:
                request (HttpRequest): La solicitud HTTP.
                email (str): El correo electrónico de la persona.

            Returns:
                JsonResponse: Una respuesta JSON con el informe de infracciones o un mensaje de error.
        """
        try:
            person = Person.objects.get(email=email)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            vehicles = person.vehicle_set.all()
            if not vehicles:
                return Response({'error': 'No vehicles found for this person'}, status=status.HTTP_404_NOT_FOUND)

            violations = Violation.objects.filter(vehicle__in=vehicles)
            if not violations:
                return Response({'message': 'No violations found for the vehicles of this person'}, status=status.HTTP_200_OK)

            serializer = ViolationSerializer(violations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
