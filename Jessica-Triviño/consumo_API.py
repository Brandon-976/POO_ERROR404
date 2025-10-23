import requests
import pandas as pd
import json
from pandas import json_normalize

link = 'https://pokeapi.co/api/v2/pokemon/ditto'
peticion = requests.get(link)
print(peticion)
pokemones = json.loads(peticion.text)
print(pokemones)

#peticion http(s) tiene estados:
#1xx (servidor la esta realizando), 2xx(todo ok), 3xx(redireccion), 4xx(error del cliente), 5xx(error del servidor)
#pip install...
