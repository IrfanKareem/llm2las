# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_response, name='generate_response'),
    path('generate_mb/', views.generate_mb, name='generate_response'),
]
