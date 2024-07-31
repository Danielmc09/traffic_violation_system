from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from officers.models import Officer
from people.models import Person
from vehicles.models import Vehicle
from violations.models import Violation
from datetime import datetime


class ViolationModelTest(TestCase):

    def setUp(self):
        # Limpiar datos previos para evitar conflictos
        Violation.objects.all().delete()
        Vehicle.objects.all().delete()
        Officer.objects.all().delete()
        User.objects.all().delete()
        Person.objects.all().delete()

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.officer = Officer.objects.create(user=self.user, name='Officer One', badge_number='12345')
        self.person = Person.objects.create(email='test@example.com', name='Test User')
        self.vehicle = Vehicle.objects.create(
            license_plate='ABC123',
            brand='Toyota',
            color='Red',
            owner=self.person
        )
        self.violation = Violation.objects.create(
            vehicle=self.vehicle,
            officer=self.officer,
            timestamp=datetime.fromisoformat('2024-07-30T15:53:00'),
            comments='Estacionado en lugar prohibido'
        )

    def test_violation_creation(self):
        self.assertTrue(isinstance(self.violation, Violation))

    def test_violation_fields(self):
        self.assertEqual(self.violation.vehicle.license_plate, 'ABC123')
        self.assertEqual(self.violation.officer.name, 'Officer One')
        self.assertEqual(self.violation.timestamp.isoformat(), '2024-07-30T15:53:00')
        self.assertEqual(self.violation.comments, 'Estacionado en lugar prohibido')

    def test_violation_update(self):
        self.violation.comments = 'Nueva infracción'
        self.violation.save()

        updated_violation = Violation.objects.get(id=self.violation.id)
        self.assertEqual(updated_violation.comments, 'Nueva infracción')

    def test_violation_delete(self):
        violation_id = self.violation.id
        self.violation.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Violation.objects.get(id=violation_id)
