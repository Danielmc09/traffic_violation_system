from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from officers.models import Officer


class OfficerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.officer = Officer.objects.create(user=self.user, name='Officer One', badge_number='12345')

    def test_officer_creation(self):
        self.assertTrue(isinstance(self.officer, Officer))
        self.assertEqual(self.officer.__str__(), self.officer.name)

    def test_officer_fields(self):
        self.assertEqual(self.officer.user.username, 'testuser')
        self.assertEqual(self.officer.name, 'Officer One')
        self.assertEqual(self.officer.badge_number, '12345')

    def test_officer_update(self):
        self.officer.name = 'Updated Officer'
        self.officer.badge_number = '54321'
        self.officer.save()

        updated_officer = Officer.objects.get(id=self.officer.id)
        self.assertEqual(updated_officer.name, 'Updated Officer')
        self.assertEqual(updated_officer.badge_number, '54321')

    def test_officer_delete(self):
        officer_id = self.officer.id
        self.officer.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Officer.objects.get(id=officer_id)
