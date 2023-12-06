from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path("cadastroLivros/", views.cadastroLivros, name='cadastroLivros'),
    path("login/", views.cadastroLivros, name='login'),
    path("categorias/", include("categories.urls", namespace="categories")),
    path("produtos/", include("products.urls", namespace="products")),
    path("redessociais/", include("socialnetworks.urls", namespace="socialnetworks")),
    path("clientes/", include("clients.urls", namespace="clients")),
    path("clientes_redessociais/", include("clients.urls", namespace="clients_socialnetworks"),),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include("books.urls")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
