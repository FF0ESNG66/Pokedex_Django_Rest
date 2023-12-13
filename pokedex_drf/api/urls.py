from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    # Available APIs
    path('pokedex/', include('pokedex.urls')),
    path('login/', include('login.urls'))
]