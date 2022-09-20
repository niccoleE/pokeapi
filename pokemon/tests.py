import datetime

import pytz

from django.test import TestCase
from django.urls import reverse

from .models import Pokemon

TEST_DATE = datetime.datetime(2017, 4, 10, 12, 00, tzinfo=pytz.utc)
TEST_IMAGE_URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png'
TEST_API_URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png'


class PokemonTests(TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon.objects.create(
            name="testPokemon_1",
            image_url=TEST_IMAGE_URL,
            api_url=TEST_API_URL,
            types=["fire"],
            date_added=TEST_DATE,
        )
        self.pokemon2 = Pokemon.objects.create(
            name="testPokemon_2",
            image_url=TEST_IMAGE_URL,
            api_url=TEST_API_URL,
            types=["fire"],
            date_added=TEST_DATE,
        )

    def test_model_str(self):
        self.assertEqual(str(self.pokemon1), 'testPokemon_1')
        self.assertEqual(str(self.pokemon2), 'testPokemon_2')

    def test_pokemons_index(self):
        response = self.client.get(reverse('pokemon:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "please Log in")

