from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
	path('nuevo/', views.asistencia_create, name='nuevo'),
	path('confirmacion/', views.asistencia_confirmacion, name='confirmacion'),
]
