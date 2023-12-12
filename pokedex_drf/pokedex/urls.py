from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.pokedex_list_create_view, name='list-create-pokedex'),
    path('<str:name>/', views.pokedex_detail_views, name='detail-pokedex'),
    path('update/<str:name>/', views.pokedex_update_view, name='update-pokedex'),
    path('delete/<str:name>/', views.pokedex_destroy_view, name='delete-pokedex'),
]