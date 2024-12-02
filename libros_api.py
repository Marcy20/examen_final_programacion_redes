#!/usr/bin/env python3

import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    """Obtiene el token de autenticación de la API."""
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic",
        auth=authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Error {r.status_code}: {r.text} al intentar autenticar.")

def addBook(book, apiKey):
    """Agrega un libro a la biblioteca usando la API."""
    r = requests.post(
        f"{APIHOST}/api/v1/books",
        headers={
            "Content-type": "application/json",
            "X-API-Key": apiKey
        },
        data=json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Libro agregado: {book['title']} por {book['author']}.")
    else:
        raise Exception(f"Error {r.status_code}: {r.text} al intentar agregar el libro {book['title']}.")

apiKey = getAuthToken()

nuevo_libro = {
    "id": 20,
    "title": "Examen Final",
    "author": "Alejandra Flore Garcia", 
}

addBook(nuevo_libro, apiKey)