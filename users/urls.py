from django.urls import path, include
from .views import LoginView, RegisterView

urlpatterns = [
    path('view/',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('getJWT/<str:userName>&<str:password>', LoginView.as_view()),
    path('register/<str:userName>', RegisterView.as_view())
]

# &<str:password>/