from django.db import models
from categories.models import Category

# Create your models here.

def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    name = models.CharField("Nome", max_length=50)
    author = models.CharField("Autor", max_length=50)
    sinopse = models.TextField("Sinopse", max_length=100)
    status = models.TextField("Status", max_length=20)
    photo = models.ImageField(upload_to='upload_image_book', blank=True) 
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["id"]
    

    def __str__(self):
        return self.name
    
    
