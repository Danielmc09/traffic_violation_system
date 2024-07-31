from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from people.models import Person


class PersonModelTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(email='test@example.com', name='Test User')

    def test_person_creation(self):
        self.assertTrue(isinstance(self.person, Person))
        self.assertEqual(self.person.__str__(), self.person.name)

    def test_person_fields(self):
        self.assertEqual(self.person.email, 'test@example.com')
        self.assertEqual(self.person.name, 'Test User')

    def test_person_update(self):
        self.person.name = 'Updated User'
        self.person.email = 'updated@example.com'
        self.person.save()

        updated_person = Person.objects.get(id=self.person.id)
        self.assertEqual(updated_person.name, 'Updated User')
        self.assertEqual(updated_person.email, 'updated@example.com')

    def test_person_delete(self):
        person_id = self.person.id
        self.person.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Person.objects.get(id=person_id)
