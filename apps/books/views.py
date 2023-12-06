from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Books

# Create your views here.


def home(request):
    books = Books.objects.all()
    return render(request, "core/index.html", {"books": books})



def salvar(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        sinopse = request.POST.get("sinopse")
        status = request.POST.get("status")
        photo = request.FILES.get("photo")

        book = Books(name=name, author=author, sinopse=sinopse, status= status, photo=photo)

        book.save()

        books = Books.objects.all()
        return render(request, "core/index.html", {"books": books})
    else:
        return render(request, "core/index.html")
    