from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.TesteView.as_view(), name='heranca'),
    path('heranca2/', views.TesteView2.as_view(), name='heranca2'),

]
