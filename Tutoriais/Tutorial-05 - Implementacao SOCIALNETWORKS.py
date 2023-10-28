####################################
########## APP socialnetworks ######
####################################

# Adicione as pastas no gitignore e "commit" e "push"

/apps/socialnetworks/__pycache__/*
/apps/socialnetworks/migrations/*

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "socialnetworks". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp socialnetworks" isso 
# tambem serve para as referencias de pastas.
# Acesse a pasta "apps" digitando o comando:

cd \apps

# Execute o comando

..\manage.py startapp socialnetworks

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o redessociais 
# do projeto "socialnetworks". Nao esqueca da virgula no final.

'socialnetworks.apps.SocialnetworksConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/socialnetworks/apps.py".
# Procure na classe "SocialnetworksConfig" o atributo "name = 'socialnetworks" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Redes Sociais'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('redessociais/', include('socialnetworks.urls', namespace='socialnetworks')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include

# Criar um "urls.py" dentro dos arquivos de configuracao do produto em "apps/socialnetworks".
# Nesse local serao declaradas as urls especificas do App socialnetworks. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialnetworks'

router = routers.DefaultRouter()
router.register('redessociais', views.SocialnetworkViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls) )
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/socialnetworks/models.py" e 
# construa seus modelos baseado no seu projeto.

# Após o comentario "# Create your models here." e crie a classe "Socialnetwork" do modelo.

class Socialnetwork(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
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
# dentro do app "socialnetworks"

from .models import Socialnetwork
from rest_framework import serializers

class SocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialnetwork
        fields = '__all__'


#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/socialnetworks/views.py" e 
# construa seus modelos baseado no seu projeto.
# Logo a seguir faça os importes dos seguintes componentes.

from .models import Socialnetwork
from rest_framework import viewsets
from .serializer import SocialnetworkSerializer

# Após o comentario "# Create your views here." e crie as views "Socialnetwork".

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer  
    
    

# Criar uma migracao do projeto a partir do modelo criado redessociais.

./manage.py makemigrations

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver


