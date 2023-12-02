from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  

# def home(request):
#     livros = Livro.objects.all()
#     return render(request, "index.html", {"livros": livros}) 


# def salvar(request):
#     name = request.POST.get("name")
#     Livro.objects.create(name=name)
#     livros = Livro.objects.all()
#     return render(request, "index.html", {"livros": livros}) 

