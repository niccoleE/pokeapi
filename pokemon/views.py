from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PokemonSerializer, UserSerializer
from .models import Pokemon

POKE_API = "http://pokeapi.co/api/v2/pokemon/"


def index(request):
    pokemons = Pokemon.objects.all()
    if request.user.is_authenticated:
        user_pokemons = Pokemon.objects.filter(owners=request.user).order_by('id')
        header = "Choose Your Pokemons"
    else:
        user_pokemons = []
        header = "To be able to choose pokemons, please Log in"
    context = {'pokemons': pokemons, 'user_pokemons': user_pokemons, 'header': header}

    return render(request, 'pokemon/index.html', context)


def my_pokemons(request, name):
    pokemon = Pokemon.objects.get(name=name)
    pokemon.owners.add(request.user)

    return redirect('pokemon:index')


def delete_pokemons(request, name):
    pokemon = Pokemon.objects.get(name=name)
    pokemon.owners.remove(request.user)

    return redirect('pokemon:index')


def profile(request):
    my_pokemons = Pokemon.objects.filter(owners=request.user).order_by('id')
    content = {'my_pokemons': my_pokemons}
    return render(request, 'pokemon/profile.html', content)


def users_info(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'pokemon/users_info.html', context)


def user_pokemons(request, username):
    user = User.objects.get(username=username)
    pokemons = Pokemon.objects.filter(owners=user)
    context = {'pokemons': pokemons}
    return render(request, 'pokemon/user_pokemons.html', context)


# api functions
@api_view(["GET"])
def api_overview(request):
    api_urls = {
        'Users List': 'api/users/',
        'User Pokemons': 'api/pokemons/{username}/',
    }
    return Response(api_urls)


@api_view(['GET'])
def users_api(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_pokemons_api(request, username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        context = {'not found': f'user with username {username} does not exist'}
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    pokemons = Pokemon.objects.filter(owners=user)
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data)
