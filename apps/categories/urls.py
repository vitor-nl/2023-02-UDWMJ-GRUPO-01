from django.urls import path, include
from . import views 
from .views import home
from rest_framework import routers

app_name = "categories"

router = routers.DefaultRouter()
router.register("categorias", views.CategoryViewSet, basename="categorias")

urlpatterns = [path("", home)]
