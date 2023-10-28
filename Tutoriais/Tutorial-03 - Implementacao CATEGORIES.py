####################################
########## APP categories ########## 
####################################

# Adicione as pastas no gitignore e "commit" e "push"

/apps/categories/__pycache__/*
/apps/categories/migrations/*

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "categories". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp categories" isso 
# tambem serve para as referencias de pastas.
# Acesse a pasta "apps" digitando o comando:

cd \apps

# Execute o comando

..\manage.py startapp categories

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o categorias 
# do projeto "categories". Nao esqueca da virgula no final.

'categories.apps.CategoriesConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/categories/apps.py".
# Procure na classe "CategoriesConfig" o atributo "name = 'categories" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Categorias'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('categorias/', include('categories.urls', namespace='categories')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include

# Criar um "urls.py" dentro dos arquivos de configuracao do categoria em "apps/categories".
# Nesse local serao declaradas as urls especificas do App categories. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'categories'

router = routers.DefaultRouter()
router.register('categorias', views.CategoryViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls) )
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/categories/models.py" e 
# construa seus modelos baseado no seu projeto.

# Após o comentario "# Create your models here." e crie a classe "Category" do modelo.

class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
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
# dentro do app "categories"

from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']



#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/categories/views.py" e 
# construa seus modelos baseado no seu projeto.
# Logo a seguir faça os importes dos seguintes componentes.

from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    
    

# Criar uma migracao do projeto a partir do modelo criado categorias.

./manage.py makemigrations

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver


