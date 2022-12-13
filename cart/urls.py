from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/puppies/<int:pk>/', get_delete_update_puppy, name = 'get_delete_update_puppy'),
    path('api/v1/puppies/', get_post_puppies, name = 'get_post_puppies')
]