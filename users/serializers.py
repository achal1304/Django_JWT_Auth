from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

    class Meta:
        model = Login
        fields = ('__all__')
        
    def create(self, validated_data):
        return Login.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.userName = validated_data.get('userName',instance.userName)
        instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance
