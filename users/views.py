from django.shortcuts import render
from rest_framework.views import APIView
from .models import Login
from .serializers import LoginSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import jwt

# Create your views here.

class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        result = Login.objects.all()
        studentSerializer = LoginSerializer(result,many = True)

        return Response({'status':'success','user':studentSerializer.data},status = 200)

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        print(request.data)
        result = Login.objects.filter(userName = request.data['userName'], password = request.data['password'])

        if result:
            encoded_jwt = jwt.encode(request.data, "secret", algorithm="HS256")
            return Response({'status':'success','jwt':encoded_jwt},status = status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','errors':'invalid username or password'},status = status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        result = Login.objects.filter(userName = request.data.get('userName'))
        serialzer = LoginSerializer(data = request.data)
        if result:
            return Response({'status':'error','data': {'userName':'same userName already exists'}},status = status.HTTP_400_BAD_REQUEST)  
        if serialzer.is_valid() and not result:
            serialzer.save()
            return Response({'status':'success','data':serialzer.data},status = status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','data':serialzer.errors},status = status.HTTP_400_BAD_REQUEST) 

    def patch(self, request, userName):
        result = Login.objects.get(userName = userName)
        serializer = LoginSerializer(result, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status = status.HTTP_201_CREATED) 
        else:
            return Response({'status':'error','data':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userName):
        result = get_object_or_404(Login,userName = userName) 
        result.delete()
        return Response({'status':'success'},status = status.HTTP_204_NO_CONTENT)  


