import json
from rest_framework.authtoken.models import Token
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import NoteUser


class TestAuthUserViewSet(TestCase):

    def setUp(self):
        self.user = mixer.blend(NoteUser)
        user = NoteUser.objects.create_superuser('user', 'user@user.ru', 'user123456')
        token, created = Token.objects.get_or_create(user=user)
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_auth_user(self):
        request = self.client.put(f'/api/v1/users/{self.user.id}/',
                                  {'username': 'username1',
                                   'email': 'user1@email.ru',
                                   })
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        user = NoteUser.objects.get(id=self.user.id)
        self.assertEqual(user.username, 'username1')
        self.assertEqual(user.email, 'user1@email.ru')

    def test_delete_auth_user(self):
        response = self.client.delete(f'/api/v1/users/{self.user.id}/', )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_details_user(self):
        user = mixer.blend(NoteUser, username='user_example')
        request = self.client.get(f'/api/v1/users/{user.id}/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        user = NoteUser.objects.get(id=user.id)
        self.assertEqual(user.username, 'user_example')


class TestGuestViewSet(TestCase):

    def setUp(self):
        self.user = mixer.blend(NoteUser)

    def test_update_other_roles(self):
        response = self.client.patch(f'/api/v1/users/{self.user.id}/', {'email': 'new_email@mail.ru', 'age': 22})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_other_role(self):
        response = self.client.patch(f'/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_details_user(self):
        response = self.client.get(f'/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
