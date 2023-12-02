from django.urls import path
from . import views
from rest_framework import routers
# from .views import home, salvar


app_name = "products"

# router = routers.DefaultRouter()
# router.register("produtos", views.ProductViewSet, basename="produtos")

urlpatterns = [
    # path("", home),
    # path('', salvar, name='salvar'),
]


