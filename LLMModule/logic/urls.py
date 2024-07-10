# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_response, name='generate_response'),
]
