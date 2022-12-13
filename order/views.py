from functools import partial
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from .models import Todo, TimingTodo
from .serializer import TodoSerializer, TimingTodoSerializer, UserSerializer



class TodoApiView(APIView):
    """
    JWT Authentication
    """
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = Todo.objects.all()
        serializer = TodoSerializer(data=result, many=True)
        if serializer.is_valid():
            return Response(
                {
                    'status': True,
                    'data': serializer.data,
                }
            )
        return Response(
            {
                'status': True,
                'data': serializer.data,
            }
        )

    def post(self, request):
        try:
            serializer = TodoSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': True,
                        'data': serializer.data,
                    }
                )
            return Response({
                'status': False,
                'data': serializer.errors,
            })

        except Exception as e:
            print(e)

        return Response(
            {
                'status': False,
                'data': 'Something went wrong'
            })
    
    def patch(self,request):
        try:
            data = request.data
            if not request.data.get('uid'):
                return Response(
                    {
                       'status': False,
                        'data': 'Missing uid'
                    }
                )
            
            result = Todo.objects.get(uid = data.get('uid'))
            serializer = TodoSerializer(result, data = data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                       'status': True,
                       'data': serializer.data,
                    })
            return Response({
                'status': False,
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'data': 'Something went wrong'
        })

class TimingTodoView(APIView):
    def get(self, request):
        result = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(result, many = True)
        return Response({
            'status': True,
            'data': serializer.data,
        })
    def post(self, request):
        try:
            serializer = TimingTodoSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                       'status': True,
                       'data': serializer.data,
                    })
            return Response({
                'status': False,
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'data': 'Something went wrong'
        })
    
@api_view(['DELETE'])
def deleteTodo(self, *args, **kwargs):
    try:
        uid = kwargs.get('uid')
        result = Todo.objects.get(uid = uid)
        if result:
            result.delete()
            return Response(
                {
                    'status': True,
                    'data': 'Todo deleted'
                },status = status.HTTP_204_NO_CONTENT
            )
        return  Response({
            'status': False,
            'data': 'UID is invalid'
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'data': 'Something went wrong'
    })

    
