from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from students.models import Student, Group


class StudentTest(TestCase):

    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get('/groups/')
        self.assertNotEqual(response.status_code, 200)
        response = self.client.post('/accounts/login/',
                                    {'username': 'admin',
                                     'password': 'admin'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, 200)

    def test_add_group(self):
        self.group = Group(
            user=User.objects.get(id=1),
            name='Test group'
        )
        self.group.save()
        group = Group.objects.get(name='Test group')
        self.assertEqual(group.id, self.group.id)
        return self.group

    def test_add_student_to_group(self):
        student = Student.objects.get(id=1)
        student.group = self.test_add_group()
        student.save()
