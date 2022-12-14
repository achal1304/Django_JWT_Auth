from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4())
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)
    class Meta:
        abstract = True

class Todo(BaseModel):
    task = models.CharField(max_length = 180)
    description = models.TextField()
    isdone = models.BooleanField(default = False)

    def get_description(self):
        return self.task + ' ' + self.description + ' ' + str(self.isdone)

class TimingTodo(BaseModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateField()