from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(requests):
    return render(requests, 'core/index.html')


@login_required
def home(requests):
    return render(requests, 'core/home.html')


@login_required
def cadastroLivros(requests):
    return render(requests, 'core/cadastroLivros.html')