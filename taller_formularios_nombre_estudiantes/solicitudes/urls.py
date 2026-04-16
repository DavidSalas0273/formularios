from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('nuevo/', views.solicitud_create, name='nuevo'),
    path('confirmacion/', views.solicitud_confirmacion, name='confirmacion'),
]
