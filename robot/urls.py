"""cloth_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from robot import views

urlpatterns = [
    path('robocategory/',
         views.RobotCategoryList.as_view(),
         name='robotcategory-list'),
    path('robocategory/<int:pk>/',
         views.RobotCategoryDetail.as_view(),
         name='robotcategory-detail'),
    path('manufacturer/',
         views.ManufacturerList.as_view(),
         name='manufacturer-list'),
    path('manufacturer/<int:pk>/',
         views.ManufacturerDetail.as_view(),
         name='manufacturer-detail'),
    path('robot/',
         views.RobotList.as_view(),
         name='robot-list'),
    path('robot/<int:pk>/',
         views.RobotDetail.as_view(),
         name='robot-detail'),
    path('',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name)
]