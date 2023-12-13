from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('login/', views.login, name='login_view'),
    path('sign_up/', views.sing_up, name='sign_up_view'),
    path('test_token/', views.test_token, name='test_token_view'),
]