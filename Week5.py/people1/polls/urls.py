from django.contrib import admin
import django.urls
from django.urls import path
from .views import index
from .views import people_Id

urlpatterns = [
    path('',index),
]