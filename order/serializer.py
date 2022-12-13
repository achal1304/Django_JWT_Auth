from dataclasses import fields
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Todo, TimingTodo
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        exclude = ['created_at']

    def get_slug(self, obj):
        return slugify(obj.task)

    def validate(self, validated_data):
        if validated_data.get('description'):
            tododescription = validated_data.get('description')
            if len(tododescription) < 10:
                raise serializers.ValidationError('description is too short') 
        return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        field = ('id','username')