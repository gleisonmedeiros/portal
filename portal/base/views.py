from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("Hello Django!!!")

def cadastro(request):
    return HttpResponse("Iniciando Cadastro")

class TesteView(TemplateView):
    template_name = "base/_test.html"

class TesteView2(TemplateView):
    template_name = "base/_test2.html"

    