from django.test import TestCase
from order.models import Todo

class TodoTest(TestCase):
    def setUp(self) -> None:
        todo = Todo.objects.create(
            task = 'This is new task',
            description = 'Test Description',
            isdone = False
        )
    
    def test_todo_description(self):
        todo = Todo.objects.get(task = 'This is new task')
        self.assertEqual(todo.get_description(), 'This is new task Test Description False')