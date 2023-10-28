####################################
########## APP orders ############ 
####################################

# Adicione as pastas no gitignore e "commit" e "push"

/apps/orders/__pycache__/*
/apps/orders/migrations/*

# Acesse a pastas "apps" e crie a estrutura basica de um projeto que 
# sera o nucleo desse projeto "orders". Como sera necessario acessar 
# a pasta "apps" o caminho da pasta manage.py pode alterar 
# dependendo do seu ambiente. 

# No linuxOS e no MacOS o caminho das barras ao contrario ""../manage.py startapp orders" isso 
# tambem serve para as referencias de pastas.
# Acesse a pasta "apps" digitando o comando:

cd \apps

# Execute o comando

..\manage.py startapp orders

# Retorne para a raiz do projeto caso ainda esteja dentro da pasta apps.

cd ..


############
# SETTINGS #
############

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o pedidos 
# do projeto "orders". Nao esqueca da virgula no final.

'orders.apps.OrdersConfig',


########
# APPS #
########

# Acesse o arquivo "apps.py" no caminho "apps/orders/apps.py".
# Procure na classe "OrdersConfig" o atributo "name = 'orders" e depois 
# desse atributo adicione a linha com o atributo com a identificao ou nome que 
# voce deseja colocar em seu aplicativo.
   
verbose_name = 'Pedidos'


########
# URLS #
########

# Na raiz do projeto acesse o arquivo "urls.py" 
# Adicione o caminho da entidade após "path('admin/', admin.site.urls),".

path('pedidos/', include('orders.urls', namespace='orders')),
path('pedidos_itens/', include('orders.urls', namespace='orders_items')),

# Altere a linha de import "from django.urls import path" adicionando o include

from django.urls import path, include


# Criar um "urls.py" dentro dos arquivos de configuracao do pedido em "apps/orders".
# Nesse local serao declaradas as urls especificas do App orders. Adicionar ao arquivo 
# as linhas a seguir.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orders'

router = routers.DefaultRouter()
router.register('pedidos', views.OrderViewSet, basename='pedidos')
router.register('pedidos_itens', views.OrderItemViewSet, basename='pedidos_itens')

urlpatterns = [
    path('', include(router.urls) )
]


##########
# MODELS #
##########

# Acesse o arquivo "models.py" no caminho "apps/orders/models.py" e 
# construa seus modelos baseado no seu projeto.

# Importe o modelo de "Product" e "Client" para adicionar o relacionamento da chave estrangeira 
# indicando a propriedade do modelo ao produtos e clientes criados.

from products.models import Product
from clients.models import Client

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.

class Order(models.Model):
    total_price = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_item = models.ManyToManyField(Product, through='OrderItem', blank=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.total_price) 


class OrderItem(models.Model):
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preco unitario',null=True, blank=True, default=0.0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.quantity) 



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
# dentro do app "orders"

from .models import Order, OrderItem
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


#########
# VIEWS #
#########

# Acesse o arquivo "views.py" no caminho "apps/orders/views.py" e 
# construa seus modelos baseado no seu projeto.
# Logo a seguir faça os importes dos seguintes componentes.

from .models import Order, OrderItem
from rest_framework import viewsets
from .serializer import OrderSerializer, OrderItemSerializer

# Após o comentario "# Create your views here." e crie as views "Order".

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer  



# Criar uma migracao do projeto a partir do modelo criado pedidos.

./manage.py makemigrations

# Executar efetivamente as migracoes criadas.

./manage.py migrate

# Inicie o servico http e teste a aplicacao no navegador.

./manage.py runserver


