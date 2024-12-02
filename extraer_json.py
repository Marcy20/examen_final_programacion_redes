import json

try:
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
except FileNotFoundError:
    print("El archivo usuarios.json no se encuentra en el directorio actual.")
    exit()
print("Nombres de los usuarios:")
for usuario in usuarios:
    print(usuario["nombre"])