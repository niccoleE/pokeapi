"""Defines URL patterns for pokemon"""

from django.urls import path

from .import views

app_name = "pokemon"

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemons/<name>', views.my_pokemons, name='my_pokemons'),
    path('pokemons/delete/<name>', views.delete_pokemons, name='delete_pokemons'),
    path('user-profile/', views.profile, name='profile'),
    path('user-info/', views.users_info, name='users_info'),
    path('pokemons/<username>/', views.user_pokemons, name='user_pokemons'),

    # api urls
    path('api/', views.api_overview, name='api_overview'),
    path('api/users/', views.users_api, name='users_api'),
    path('api/pokemons/<username>/', views.user_pokemons_api, name='user_pokemons_api'),

]