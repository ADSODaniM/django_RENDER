from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.lista_servicios, name='servicios'),
    path('servicios/<int:servicio_id>/', views.detalle, name='detalle'),


]