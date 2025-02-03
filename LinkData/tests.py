from django.test import TestCase
from . import views
from django.urls import path
# Create your tests here.
urlpatterns = [
    path('',views.convert_into_app, name='home')
]