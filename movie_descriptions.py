import os
import json
from PIL import Image
from io import BytesIO
import numpy as np
from dotenv import load_dotenv

import google.generativeai as genai
import requests

# Se leen las claves API desde el archivo .env
_ = load_dotenv('api_keys.env')
genai.configure(api_key=os.environ.get('gemini_api_key'))
hf_api_key = os.environ.get('hf_api_key')


# Se carga la lista de películas desde el archivo movie_titles.json
with open('movie_titles.json', 'r') as file:
    file_content = file.read()
    movies = json.loads(file_content)



# Selecciona un modelo de Google Generative AI
model = genai.GenerativeModel('gemini-pro')

# Selección aleatoria de una película
idx_movie = np.random.randint(len(movies) - 1)
movie = movies[idx_movie]
movie_title = movie["title"]
print(f"Título de la película seleccionada: {movie_title}")

# Instrucción para la IA generativa
instruction = """
Vas a actuar como un aficionado del cine que sabe describir de forma clara, concisa y precisa cualquier película en menos de 200 palabras. 
La descripción debe incluir el género de la película y cualquier información adicional que sirva para crear un sistema de recomendación.
"""


# Crear el prompt
prompt = f"{instruction} Haz una descripción de la película {movie_title}"

# Generar la descripción con Google Generative AI
response = model.generate_content(prompt)

# Mostrar la descripción generada
print(f"Descripción generada: {response.text}")

#######################################################



# Podemos iterar sobre todas las películas para generar la descripción. Dado que esto 
#puede tomar bastante tiempo, el archivo con las descripciones para todas las películas es movie_descriptions.json
""""
for i in range(len(movies)):
    prompt =  f"{instruction} Has una descripción de la película {movies[i]['title']}"
    response = get_completion(prompt)
    movies[i]['description'] = response 
    prompt = f"{instruction_genre} Género de la película {movies[i]['title']}"
    response = get_completion(prompt)
    movies[i]['genre'] = response   
    prompt = f"{instruction_year} Año de lanzamiento de la película {movies[i]['title']}"
    response = get_completion(prompt)
    movies[i]['year'] = response
    print(movies[i]['title'])
    print(movies[i]['genre'])
    print(movies[i]['year'])

    print(f"pelicula {i} de {len(movies)}")

file_path = "movie_descriptions.json"

# Write the data to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(movies, json_file, indent=4)  # The 'indent' parameter is optional for pretty formatting

print(f"Data saved to {file_path}")
"""