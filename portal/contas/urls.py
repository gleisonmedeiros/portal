from django.urls import path
from django.contrib.auth import views as auth_views
from contas.views import UserLoginView


urlpatterns = [
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
]