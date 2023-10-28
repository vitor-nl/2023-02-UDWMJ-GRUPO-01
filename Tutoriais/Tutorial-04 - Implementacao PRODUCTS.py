####################################
########## APP products ############ 
####################################

# Adicione as pastas no gitignore e "commit" e "push"

/apps/products/__pycache__/*
/apps/products/migrations/*

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "products". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp products" isso 
# tambem serve para as referencias de pastas.
# Acesse a pasta "apps" digitando o comando:

cd \apps

# Execute o comando

..\manage.py startapp products

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o produtos 
# do projeto "products". Nao esqueca da virgula no final.

'products.apps.ProductsConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/products/apps.py".
# Procure na classe "ProductsConfig" o atributo "name = 'products" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Produtos'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('produtos/', include('products.urls', namespace='products')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include

# Criar um "urls.py" dentro dos arquivos de configuracao do produto em "apps/products".
# Nesse local serao declaradas as urls especificas do App products. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'products'

router = routers.DefaultRouter()
router.register('produtos', views.ProductViewSet, basename='produtos')

urlpatterns = [
    path('', include(router.urls) )
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/products/models.py" e 
# construa seus modelos baseado no seu projeto.

# Importe o modelo de "Category" para adicionar o relacionamento da chave estrangeira 
# indicando a propriedade do modelo ao categorias criado.

from categories.models import Category

# Após o comentario "# Create your models here." e crie a classe "Product" do modelo.

class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name


####################################################
#                 serializers                      #
# Conversao dos dados de banco de dados em formato #
# json para que os agentes externos entendam o     #
# formado de dados. O serializer que permite que   #
# dados sejam convertidos para a forma Python      #
# nativa, de modo que o RM do Python entenda, e    #
# que sejam facilmente renderizados em JSON, XML,  #
# ou outros tipos.                                 #
####################################################

# Cria o arquivo "serializer.py" do Django Rest Framework 
# dentro do app "products"

from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/products/views.py" e 
# construa seus modelos baseado no seu projeto.
# Logo a seguir faça os importes dos seguintes componentes.

from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  


# Criar uma migracao do projeto a partir do modelo criado produtos.

./manage.py makemigrations

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver


