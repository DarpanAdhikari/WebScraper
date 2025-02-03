from django.urls import path
from . import views
urlpatterns = [
    path('',views.convert_into_app, name='index'),
    path('fetch-content/',views.fetch_content, name='fetch'),
]
