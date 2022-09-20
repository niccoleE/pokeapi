from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PokemonSerializer, UserSerializer
from .models import Pokemon


def index(request):
    response = requests.get("http://pokeapi.co/api/v2/pokemon?limit=50").json()
    pokemons = response['results']

    if request.user.is_authenticated:
        user_pokemons = Pokemon.objects.filter(owners=request.user).order_by('id')
        user_pokemon_names = [p.name for p in user_pokemons]
        header = "Choose Your Pokemons"
    else:
        user_pokemon_names = []
        header = "To be able to choose pokemons, please Log in"

    context = {'pokemons': pokemons, 'names': user_pokemon_names, 'header': header}
    return render(request, 'pokemon/index.html', context)

def my_pokemons(request, name):
    pokemon_url = ""
    response = requests.get("http://pokeapi.co/api/v2/pokemon?limit=50").json()
    pokemons = response['results']

    for pokemon in pokemons:
        if pokemon['name'] == name:
            pokemon_url = pokemon['url']
            pokemon['in_db'] = "yes"

    pokemon_data = requests.get(pokemon_url).json()
    pokemon_name = pokemon_data['name']
    pokemon_img = pokemon_data['sprites']['front_default']
    pokemon_types = [t['type']['name'] for t in pokemon_data['types'] if pokemon_data['types']]

    new_pokemon = Pokemon(
        name=pokemon_name,
        image_url=pokemon_img,
        api_url=pokemon_url,
        types=pokemon_types,
    )
    try:
        new_pokemon.save()
        new_pokemon.owners.add(request.user)
    except IntegrityError:
        this_pokemon = Pokemon.objects.get(name=name)
        this_pokemon.owners.add(request.user)

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
    the_user = User.objects.get(username=username)
    pokemons = Pokemon.objects.filter(owners=the_user)
    context = {'pokemons': pokemons, 'the_user': the_user}
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
