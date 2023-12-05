from django.contrib import admin
from django.urls import path, include
from .views import home, salvar

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    # path('delete/<int:id>', editar, name="editar"),
    # path('your-url/', views, name='modal_view'),
]