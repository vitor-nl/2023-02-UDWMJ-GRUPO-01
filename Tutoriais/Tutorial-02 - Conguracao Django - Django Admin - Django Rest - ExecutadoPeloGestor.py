####################################################
#                 SOFTWARES                        #
# Instalacao de softwares para desenvolvimento de  #
# software utilizando Framework Django             #
# e banco de dados PostgreSQL.                     #
####################################################

# Baixar e instalar Python3.* e nao esquecer de marcar 
# para a adicionar ao Path ou as variaveis de ambiente
# do Sistema Operacional.

https://www.python.org/

# Baixar e instalar o VSCode.

https://code.visualstudio.com/

# Instalar através do VSCode as Extensoes a seguir.

"GitHub Pull Requests and Issues"
"Python for VSCode"

# Baixar e instalar o Git  e nao 
# esquecer de marcar para a "Adicionar ao Path" ou as
# variaveis de ambiente do Sistema Operacional.

https://git-scm.com/

# Baixar e instalar o SGBD Postgres

https://www.postgresql.org/download/

# Baixar e instalar Miniconda para Python3.*. e nao 
# esquecer de marcar para a adicionar ao Path ou as
# variaveis de ambiente do Sistema Operacional.

https://docs.conda.io/ 

# Apos a instalcao adicione o conda ao manualmente no
# Path do Windows em variaveis de ambiente.

C:\Users\user\miniconda3\Scripts\activate.bat C:\Users\user\miniconda3


############################################
#                  MINICONDA               #
# Criacao de Ambiente virtual isolado para #
# instalacao das bibliotecas necessarias   #
# para o desenvolvimento do projeto        #
############################################

# Crie uma diretorio de nome "projetos".
# Abra o vscode esse diretorio.
# Abra dentro do VSCode o "Command Prompt" do windows
# Na aba do VSCode: view -> Command Pallete 
# procure por "Python: Select Interpreter"
# e selecione a versao do python instalado.

# Nos laboratorios da Uniritter antes de qualquer 
# procedimento deve-se rodar esse script

%windir%\System32\cmd.exe "/K" C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3

%windir%\System32\cmd.exe "/K" C:\Users\79leo\miniconda3\Scripts\activate.bat C:\Users\79leo\miniconda3
# Caso não funcione o de cima



# Criar ambiente virtual de desenvolvimento (Defina
# um nome seguido pela palavra app, por exmeplo "lojaapp"
# ou "projetoapp").

conda create -n nome_do_projeto_que_voce_escolher

# Liste os ambientes criados.

conda env list

# Remover ambiente virtual de desenvolvimento.

conda env remove -n nome_do_projeto_que_voce_escolher 

# Ative o ambiente criado. 
# Verifique se no início da linha comandos aparece o nome 
# do projeto entre parenteses conforme o seguinte exemplo
# "(modeloapp) Antonio:~ antonio$".

conda activate nome_do_projeto_que_voce_escolher

# Desative o ambiente. 
# Verifique se no início da linha de comandos desaparece
# o nome entre parenteses conforme o seguinte exemplo 
# "Antonio:~ antonio$".

conda deactivate


#######################################################
# As etapas a seguir devem ser executadas dentro      #
# do ambiente virtual de desenvolvimento do miniconda #
# para cada projeto. Ou seja com o conda atividado    #
# como por exemplo "(modeloapp) Antonio:~ antonio$"	  #
#######################################################

#############################################
# Instalação de bibliotecas Python e Djando #
#############################################

# Utilizar o terminal(Command Prompt) do VSCODE faça todas as 
# operacoes (Para os usuarios de windows nao utilize o PowerShell)

# Instalar o PIP atraves do Miniconda para gerenciamento de pacotes padrao  
# e usado para instalar e gerenciar pacotes de software escritos em Python 
# (A regra para instalação de pacotes, bibliotecas  e dependências, será 
# sempre instalar com o MINICONDA e caso nao tenha utilizar o PIP).

conda install pip

# Instalar Biblioteca "python-decouple" para esconder informações 
# importantes por segurança como as de banco de dados e chave de
# registro do sistema em um arquivo separado chamado exatamente de
# ".env" com essas informações.

pip install python-decouple

# Instalar Biblioteca do driver do banco de dados postgres 
# "psycopg2-binary" para rodar no Framework Django.

pip install psycopg2-binary 

# Instalar o Framework Django.

conda install django


############################################
# Conferência de instalação de Bibliotecas #
############################################

# Digite o comando para listas as bibliotecas instaladas.

pip list

# Digite o comando para listas as bibliotecas instaladas.

conda list


##############################################
# Criacao e configuracao do Framework Django #
##############################################

# Crie um projeto Django em um diretório de sua escolha onde
# ficarao todos os seus projetos (Defina com o mesmo nome do 
# ambiente virtual por exmeplo "lojaapp" ou "projetoapp").

django-admin startproject nome_do_projeto_que_voce_escolher

# O comando criará a seguinte estrutura de pastas.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .   
      ├── manage.py
      └── nome_do_projeto_que_voce_escolher
          ├── __init__.py
          ├── asgi.py
          ├── settings.py
          ├── urls.py
          └── wsgi.py

# Acesse o diretorio RAIZ do projeto criado, e através do 
# terminal inicie o serviço do Django. Lembre que dependendo
# do sitema operacional o "manage.py" pode ser executado de
# forma diferente, por exemplo sem o "./" .

./manage.py runserver

# Depedendo da forma que o python foi instalado ele precisa 
# ser executado com a chamada do Python na frente.

python manage.py runserver

# Acessar um navegador de sua escolha, digitar para testar o 
# servico de servidor web socket criado pelo django.

http://localhost:8000

# Para parar o serviço.

Ctrl + C 

# Caso desejar iniciar o serviço utilizando outra porta
#  como por exemplo 8001.

python ./manage.py runserver 8001

#################################################
# Acesso PostgreSQL e Criação do Banco de dados #
#################################################

# Acesse o postgres via PgAdmin, PSQL ou outro porgrama de sua escolha.

# Utilizando PgAdmin:
# Acesse o diretorio de instalação do PostgrSQL e utilize a interface 
# grafica para definir um nome de usuario, senha e os privilegios 
# necessarios. Como nao e recomendado utilizar o usuario de senha 
# de administador o recomendado é criar uma regra/usuario no postgres.
# defina um nome intuitivo como nome_do_projeto_que_voce_escolher_user
# e nome_do_projeto_que_voce_escolher_db.

# Criando um usuario para o banco de dados.

Servers >> PostgreSQL 13 >> Botão direito mouse >> create >> Login/Group Role

# Cria um banco de dados.

Servers >> PostgreSQL 13 >> Databases >> botao direito mouse >> create

# Vincule o usuario ao banco dea dados criado.

nome_do_projeto_que_voce_escolher_db >> Properties >> Security


#######################################################
# As etapas a seguir devem ser executadas dentro      #
# do ambiente virtual de desenvolvimento do miniconda #
# para cada projeto. Ou seja com o conda atividado    #
# como por exemplo "(modeloapp) Antonio:~ antonio$"	  #
#######################################################

#########################################################
#### Raiz de projetos e Gerenciador Framework Django ####
#########################################################

# Acesse o diretorio de seus projetos e crie um projeto Framework Django

django-admin startproject nome_do_projeto_que_voce_escolher

# Observe a raiz do diretorio craido a partir do comando e 
# arvore de diretorios criada para o projeto basico do Django.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .   
      ├── manage.py
      └── nome_do_projeto_que_voce_escolher (CONFIGURAÇÕES GERAIS)
          ├── __init__.py
          ├── asgi.py
          ├── settings.py
          ├── urls.py
          └── wsgi.py

# Inicializar o servico (Dependendo do servico sistema o 
# comando pode mudar ".\manage.py runserver").

python manage.py runserver

# Após o comando "manage.py runserver" o django criar um diretorio de 
# cache e um banco de dados nativo local "db.sqlite". O cache sao os
# logs e o banco sqlite nao sera utilizado por ser local e a melhor
# alternativa sempre sera banco de dados distribuidos ou em servidores.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .
      ├── nome_do_projeto_que_voce_escolher
      │   ├── __init__.py
      │   ├── __pycache__
      │   │   ├── __init__.cpython-39.pyc
      │   │   ├── settings.cpython-39.pyc
      │   │   ├── urls.cpython-39.pyc
      │   │   └── wsgi.cpython-39.pyc
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── db.sqlite3
      └── manage.py
 
# Atraves do arquivo "manage.py" que as operacoes do Django so gerenciadas,
# por exemplo o comando de inicializar serviCo do socket do protocolo
# dere de http "python manage.py runserver".


############################################
# Desenvolvimento do projeto no IDE VSCode #
############################################

# Abrir VSCode.

# Open Folder e procurar o projeto RAIZ em seu computador e abrir.

  (RAIZ)nome_do_projeto_que_voce_escolher
      .
      ├── nome_do_projeto_que_voce_escolher
      │   ├── __init__.py
      │   ├── __pycache__
      │   │   ├── __init__.cpython-39.pyc
      │   │   ├── settings.cpython-39.pyc
      │   │   ├── urls.cpython-39.pyc
      │   │   └── wsgi.cpython-39.pyc
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── db.sqlite3
      └── manage.py


#######################
# Arquivo settings.py #
#######################

# O arquivo settings.py do Django e o local responsavel por todas
# as configuracoes gerais do framework django e suas declaracoes de 
# caminhos do sistemas para o desenvolvimento do software.

######################################################
# Configurações gerais do Django e do banco de dados #
######################################################

# No VSCode abra o arquivo de configurações do Django "settings.py".

# No "settings.py" no inicio do arquivo importar a modulo "OS" antes 
# do "from pathlib import Path". Serve para manipular funcionalidades
# do sistema operacional.

import os

# No "settings.py" no inicio do arquivo importar modulo "SYS" apos 
# "import os". Fornece funcoes e variaveis ​​usadas para manipular 
# partes do ambiente de tempo de execucao do Python.

import sys 

# No "settings.py" procure pela linha "from pathlib import Path" e 
# apos digite a linha a seguir para importar a biblioteca "decouple" 
# que server para esconder os dados de conexao do postgres garantindo 
# a seguranca.

from decouple import config

# No "settings.py" procure pela linha "BASE_DIR". Essa alteracao 
# muda o caminho do path dos diretorios de acesso do django.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# No "settings.py" procure pela linha "SECRET_KEY" copie a chave de 
# seguranca que esta entre aspas e salve em um lugar seguro (Nao perca 
# a chave em hipotese alguma). Apos guardar a chave aleatorio substitua
# a linha pela seguinte descricao. Esse processo garantiara a seguranca
# do projeto.

SECRET_KEY = config('SECRET_KEY')

# No "settings.py" procure pela linha "DEBUG" e substitua a linha pela
# seguinte descricao. Esse procedimento tambem sera passado para um
# arquivo que ficara oculto.

DEBUG = config('DEBUG', default=False, cast=bool)

# "No "settings.py" procure pela linha DATABASES onde encontrara as 
# configurações do sqlite3, banco de dados local nativo do Djando. 
# Todo o conteudo devera ser substituido pelas seguintes informacoes
# de forma que os dados de acesso serao colocados em um arquivo de 
# CONFIG oculto assim como os dados do SECRET_KEY e DEBUG.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),    
        'PORT': config('DB_PORT'),     
    }
}

# Esses procedimentos permitiram esconder as informacoes 
# importantes de seguranca. Agora para finalizar vamos criar
# esse arquivo de configuracao.
# Criar um arquivo no o nome especifico de ".env" na raiz do 
# projeto "(RAIZ)nome_do_projeto_que_voce_escolher" e inserir 
# as informacoes a seguir e salvar.

SECRET_KEY=Copiar a chave aleatoria salva e cole aqui sem aspas
DEBUG=True
DB_NAME=nome_banco_de_dados
DB_USER=nome_de_usuario_de_acesso_ao_banco
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432

# Altere no arquivo "settings.py" o idioma 
# e o horário que usaremos na aplicação, 
# procure e altere as seguintes linhas de 
# código "LANGUAGE_CODE" e "TIME_ZONE":

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'


# Teste o ambiente Django

python manage.py runserver

# Acesse um navegador de Internet e digite o endereco:

http://127.0.0.1:8000/ 

# ou 

http://localhost:8000/


#############################################################
##### Migracoes e Geracao de entidades no banco de dados ####
#############################################################

# Django Framework trabalha com Mapeamento Objeto-Relacional(ORM) 
# para percistencia de dados e migra as aplicacões existentes do 
# Django atraves das classes dos objetos criados gerando o banco 
# de dados baseado nessa estrutura.

# Comando de migracao necessario apos alteracoes nos objetos sao:
# "makemigrations" e "migrate".

python manage.py migrate

# Criar um usuario dentro da aplicacao do admin do Django.

python manage.py createsuperuser

# Defina o nome de usuario "admin", um email e senha valida
# sugestao "123456" e confirmar.
# Acesse um navegador de Internet e digite o endereco.
# Acessar o admin com os usuario e senha criados.

http://127.0.0.1:8000/ 

# ou 

http://localhost:8000/


##############################
# settings.py  Configuracoes #
##############################

# Crie uma pasta "apps" na raiz do projeto.
# Acesse o arquivo "settings.py" e procure por BASE_DIR e 
# adicione as linhas seguintes para registrar os caminhos 
# onde os APPs ficarao, o django trabalha com APPs e para 
# cada entidade são criados APPs e seus objetos dentro de 
# sua composicao.

APPS_DIR = os.path.join(BASE_DIR, 'apps') 
sys.path.insert(0, APPS_DIR) 


####################################################
#                 SOFTWARES                        #
# Instalacao de softwares para desenvolvimento de  #
# software relacionados ao Django Rest Framework . #
####################################################

# Instalcao do Django Rest Framework.

pip install djangorestframework

# Instalacao Markdown, suporte para o navegador rodar as API
# tratase de um conversor.

pip install markdown   

# Instalcao diango-filter que serve para aliviar a escrita de 
# alguns dos bits em relacao de códigos de visualização.

pip install django-filter

# Acesse o arquivo "settings.py" e procure por INSTALLED_APPS e adicione 
# dentro dos colchetes a nova linha a seguir para declarar o Django rest
# framework. Nao esqueca das virgula no final.

'rest_framework',

# Teste o funcionamento dos Ambientes

http://127.0.0.1:8000/ 

# ou 

http://localhost:8000/