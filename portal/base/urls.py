from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
