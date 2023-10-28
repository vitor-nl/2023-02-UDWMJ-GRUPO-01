###################################
########## APP clients ############ 
###################################

# Adicione as pastas no gitignore e "commit" e "push"

/apps/clients/__pycache__/*
/apps/clients/migrations/*

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "clients". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp clients" isso 
# tambem serve para as referencias de pastas.
# Acesse a pasta "apps" digitando o comando:

cd \apps

# Execute o comando

..\manage.py startapp clients

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o clientes 
# do projeto "clients". Nao esqueca da virgula no final.

'clients.apps.ClientsConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/clients/apps.py".
# Procure na classe "ClientsConfig" o atributo "name = 'clients" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Clientes'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('clientes/', include('clients.urls', namespace='clients')),
path('clientes_redessociais/', include('clients.urls', namespace='clients_socialnetworks')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include

# Criar um "urls.py" dentro dos arquivos de configuracao do produto em "apps/clients".
# Nesse local serao declaradas as urls especificas do App clients. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clients'

router = routers.DefaultRouter()
router.register('clientes', views.ClientViewSet, basename='clientes')
router.register('clientes_redessociais', views.ClientSocialnetworkViewSet, basename='clientes_redessociais')

urlpatterns = [
    path('', include(router.urls) )
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/clients/models.py" e 
# construa seus modelos baseado no seu projeto.

# Importe o modelo de "Socialnetwork" depois do "from django.db import models" para 
# adicionar o relacionamento da chave estrangeira indicando a propriedade
# do modelo ao socialnetworks criado.

from socialnetworks.models import Socialnetwork

# Após o comentario "# Create your models here." e crie a classe "Client" do modelo.

class Client(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    client_socialnetwork = models.ManyToManyField(Socialnetwork, through='ClientSocialnetwork', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name



class ClientSocialnetwork(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(Socialnetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Redes Social'
        verbose_name_plural = 'Itens de Rede Social'
        ordering =['id']

    def __str__(self):
        return self.socialnetwork.name 


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
# dentro do app "clients"

from .models import Client, ClientSocialnetwork
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialnetwork
        fields = '__all__'

#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/clients/views.py" e 
# construa seus modelos baseado no seu projeto.
# Logo a seguir faça os importes dos seguintes componentes.

from .models import Client, ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSerializer, ClientSocialnetworkSerializer

# Após o comentario "# Create your views here." e crie as views "Client".

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer



# Criar uma migracao do projeto a partir do modelo criado clientes.

./manage.py makemigrations

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver


