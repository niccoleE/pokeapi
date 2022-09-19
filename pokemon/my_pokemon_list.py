pokemon_list = [
        {'name': 'bulbasaur',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/1'},
        {'name': 'ivysaur',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/2'},
        {'name': 'venusaur',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/3'},
        {'name': 'charmander',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/4'},
        {'name': 'charmeleon',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/5'},
        {'name': 'charizard',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/6'},
        {'name': 'squirtle',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/7'},
        {'name': 'wartortle',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/8'},
        {'name': 'blastoise',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/9'},
        {'name': 'caterpie',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/10'},
        {'name': 'metapod',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/11'},
        {'name': 'butterfree',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/12'},
        {'name': 'weedle',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/13'},
        {'name': 'kakuna',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/14'},
        {'name': 'beedrill',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/15'},
        {'name': 'pidgey',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/16'},
        {'name': 'pidgeotto',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/17'},
        {'name': 'pidgeot',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/18'},
        {'name': 'rattata',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/19'},
        {'name': 'raticate',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/20'},
        {'name': 'spearow',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/21.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/21'},
        {'name': 'fearow',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/22.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/22'},
        {'name': 'ekans',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/23'},
        {'name': 'arbok',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/24'},
        {'name': 'pikachu',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/25'},
        {'name': 'raichu',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/26'},
        {'name': 'sandshrew',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/27'},
        {'name': 'sandslash',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/28'},
        {'name': 'nidoran-f',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/29.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/29'},
        {'name': 'nidorina',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/30'},
        {'name': 'nidoqueen',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/31.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/31'},
        {'name': 'nidoran-m',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/32.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/32'},
        {'name': 'nidorino',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/33.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/33'},
        {'name': 'nidoking',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/34.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/34'},
        {'name': 'clefairy',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/35'},
        {'name': 'clefable',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/36'},
        {'name': 'vulpix',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/37'},
        {'name': 'ninetales',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/38'},
        {'name': 'jigglypuff',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/39'},
        {'name': 'wigglytuff',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/40'},
        {'name': 'zubat',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/41.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/41'},
        {'name': 'golbat',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/42.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/42'},
        {'name': 'oddish',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/43.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/43'},
        {'name': 'gloom',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/44.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/44'},
        {'name': 'vileplume',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/45.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/45'},
        {'name': 'paras',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/46.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/46'},
        {'name': 'parasect',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/47.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/47'},
        {'name': 'venonat',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/48.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/48'},
        {'name': 'venomoth',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/49.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/49'},
        {'name': 'diglett',
         'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png',
         'pokemon_url': 'http://pokeapi.co/api/v2/pokemon/50'},
    ]

i = 1
for p in pokemon_list:
    p['pok_id'] = i
    i += 1

# <p>{{ pokemon.name }}<a class="btn btn-outline-success" href="{% url 'pokemon:my_pokemons' pokemon.pok_id %}">Add to My Pokemons</a>