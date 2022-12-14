from datetime import datetime
from django.test import TestCase
from order.models import Todo, User
from order.views import TodoApiView
from order.serializer import TodoSerializer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import uuid
import json

user = User.objects.get(username = 'achal')
client = APIClient()
client.force_authenticate(user = user)
class TodoApiViewTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            uid = uuid.uuid4(),
            created_at = datetime.now(),
            updated_at = datetime.now(),
            task = 'Test Task',
            description = 'Test Description',
            isdone = False
        )
        self.valid_payload = {
            'uid' : str(uuid.uuid4()),
            'created_at' : str(datetime.now()),
            'updated_at' : str(datetime.now()),
            'task' : 'Test1 Task',
            'description' : 'Test1 Description',
            'isdone' : False
        }
        self.invalid_payload = {
            'uid' : str(uuid.uuid4()),
            'created_at' : str(datetime.now()),
            'updated_at' : str(datetime.now()),
            'task' : 'Test1 Task',
            'description' : 'Descr',
            'isdone' : False
        }
    
    def test_get_valid_todo(self):
        response = client.get(reverse('get_post_put_todos'))
        testtodos = Todo.objects.all()
        todoSerializer = TodoSerializer(testtodos,many = True)
        self.assertEqual(todoSerializer.data, response.data['data'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_valid_todo(self):
        response = client.post(
            reverse('get_post_put_todos'),
            data = json.dumps(self.valid_payload),
            content_type = 'application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_todo(self):
        response = client.post(
            reverse('get_post_put_todos'),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

