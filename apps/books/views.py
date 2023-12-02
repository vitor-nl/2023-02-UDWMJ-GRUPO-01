from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Books

# Create your views here.


def home(request):
    books = Books.objects.all()
    return render(request, "books.html", {"books": books})


def views(request):
    context = {}
    if request.method == "POST":
        # Handle form submission logic
        pass
    return render(request, "books.html", context)


# def salvar(request):
#     name = request.POST.get("name")
#     # author = request.POST.get("author")
#     sinopse = request.POST.get("sinopse")
#     # status = request.POST.get("status")
#     # date_fabrication = request.POST.get("date_fabrication")
#     active = request.POST.get("active")
#     Books.objects.create(name=name)
#     # Books.objects.create(author=author)
#     Books.objects.create(sinopse=sinopse)
#     # Books.objects.create(status=status)
#     # Books.objects.create(date=date_fabrication)
#     # Books.objects.create(date=date_fabrication)
#     books = Books.objects.all()
#     return render(request, "books.html", {"books": books})


def salvar(request):
    if request.method == "POST":
        # Get all form data
        name = request.POST.get("name")
        author = request.POST.get("author")
        sinopse = request.POST.get("sinopse")
        status = request.POST.get("status")
        # date_fabrication = request.POST.get("date_fabrication")
        # active = request.POST.get("active")

        book = Books(name=name, author=author, sinopse=sinopse, status= status)

        book.save()

        books = Books.objects.all()
        return render(request, "books.html", {"books": books})
    else:
        return render(request, "books.html")
    
    # def editar(request, id):
    #     books = Books.objects.get(id=id)
    #     return render(request, "update.html", {"books": books})