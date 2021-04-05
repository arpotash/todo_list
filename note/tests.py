from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from note.models import Project, TODO
from user.models import NoteUser


class TestProjectViewSetAuthUser(TestCase):

    def setUp(self):
        self.project = mixer.blend(Project)
        user = NoteUser.objects.create_superuser('user', 'user@user.ru', 'user123456')
        token, created = Token.objects.get_or_create(user=user)
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        request = self.client.post('/api/projects/',
                                   {'name': 'project_example',
                                    'users': [1, 2],
                                    'url': 'http://project.repo',
                                    })
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        print()

    def test_update_project(self):
        request = self.client.patch(f'/api/projects/{self.project.id}/',
                                    {'name': 'update_project_example',
                                     'users': self.project.users,
                                     'url': 'http://update-project.repo',
                                     })
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        request = self.client.delete(f'/api/projects/{self.project.id}/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_details_project(self):
        project = mixer.blend(Project, name='project_example')
        request = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'project_example')


class TestProjectViewSetGuest(TestCase):

    def setUp(self):
        self.project = mixer.blend(Project)

    def test_update_other_roles(self):
        response = self.client.patch(f'/api/projects/{self.project.id}/',
                                     {'name': 'update_project_example',
                                      'users': self.project.users,
                                      'url': 'http://update-project.repo',
                                      })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_other_role(self):
        response = self.client.patch(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_details_project(self):
        response = self.client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestTodoViewSetAuthUser(TestCase):

    def setUp(self):
        self.todo = mixer.blend(TODO)
        user = NoteUser.objects.create_user('user', 'user@user.ru', 'user123456')
        token, created = Token.objects.get_or_create(user=user)
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_list(self):
        request = self.client.get('/api/notes/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        request = self.client.post('/api/notes/',
                                   {'project': self.todo.project.id,
                                    'creator': self.todo.creator.id,
                                    'text': 'description task'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_update_todo(self):
        request = self.client.put(f'/api/notes/{self.todo.id}/',
                                  {'project': self.todo.project.id,
                                   'creator': self.todo.creator.id,
                                   'text': 'update_task'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        todo = TODO.objects.get(id=self.todo.id)
        self.assertEqual(todo.text, 'update_task')

    def test_partial_update_todo(self):
        request = self.client.patch(f'/api/notes/{self.todo.id}/',
                                    {'text': 'update_task'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        todo = TODO.objects.get(id=self.todo.id)
        self.assertEqual(todo.text, 'update_task')

    def test_delete_todo(self):
        request = self.client.delete(f'/api/notes/{self.todo.id}/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        todo = TODO.objects.get(id=self.todo.id)
        self.assertEqual(todo.is_active, False)

    def test_details_todo(self):
        todo = mixer.blend(TODO, text='task_example')
        request = self.client.get(f'/api/notes/{self.todo.id}/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        todo = TODO.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'task_example')


class TestTodoViewSetGuest(TestCase):

    def setUp(self):
        self.todo = mixer.blend(TODO)

    def test_get_list(self):
        request = self.client.get('/api/notes/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_todo(self):
        request = self.client.post('/api/notes/',
                                  {'project': self.todo.project.id,
                                   'creator': self.todo.creator.id,
                                   'text': 'description task'})
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_todo(self):
        request = self.client.put(f'/api/notes/{self.todo.id}/',
                                  {'project': self.todo.project.id,
                                   'creator': self.todo.creator.id,
                                   'text': 'description task'})
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update_todo(self):
        request = self.client.patch(f'/api/notes/{self.todo.id}/',
                                  {'text': 'description task'})
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_todo(self):
        request = self.client.get(f'/api/notes/{self.todo.id}/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_details_todo(self):
        todo = mixer.blend(TODO, text='task_example')
        request = self.client.get(f'/api/notes/{self.todo.id}/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)