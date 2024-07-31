from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from people.models import Person
from vehicles.models import Vehicle


class VehicleModelTest(TestCase):

    def setUp(self):
        # Limpiar datos previos para evitar conflictos de unicidad
        Vehicle.objects.all().delete()
        Person.objects.all().delete()

        self.person = Person.objects.create(email='test@example.com', name='Test User')
        self.vehicle = Vehicle.objects.create(
            license_plate='ABC123',
            brand='Toyota',
            color='Red',
            owner=self.person
        )

    def test_vehicle_creation(self):
        self.assertTrue(isinstance(self.vehicle, Vehicle))
        self.assertEqual(self.vehicle.__str__(), self.vehicle.license_plate)

    def test_vehicle_fields(self):
        self.assertEqual(self.vehicle.license_plate, 'ABC123')
        self.assertEqual(self.vehicle.brand, 'Toyota')
        self.assertEqual(self.vehicle.color, 'Red')
        self.assertEqual(self.vehicle.owner.email, 'test@example.com')

    def test_vehicle_update(self):
        self.vehicle.brand = 'Honda'
        self.vehicle.color = 'Blue'
        self.vehicle.save()

        updated_vehicle = Vehicle.objects.get(id=self.vehicle.id)
        self.assertEqual(updated_vehicle.brand, 'Honda')
        self.assertEqual(updated_vehicle.color, 'Blue')

    def test_vehicle_delete(self):
        vehicle_id = self.vehicle.id
        self.vehicle.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Vehicle.objects.get(id=vehicle_id)
