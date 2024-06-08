"""Desarrollo del punto 3"""

import requests
#Método get
response_get = requests.get(url='https://jsonplaceholder.typicode.com/users', timeout=10)
users = response_get.json()
print(users)
data = {
    'name': 'Estiben',
    'email': 'estibengon@email.com',
    'username': 'EstibenGon'
}
#Método put
response_put = requests.put(url='https://jsonplaceholder.typicode.com/users/1',
                        json=data,
                        timeout=10)

if response_put.status_code == 200:
    print("Usuario actualizado correctamente")
else:
    print(f"Error al actualizar el usuario. Código de respuesta: {response_put.status_code}")
# Método patch
response_patch = requests.patch(url='https://jsonplaceholder.typicode.com/users/1',
                                json=data,
                                timeout=10)

if response_patch.status_code == 200:
    print("Usuario actualizado correctamente")
else:
    print(f"Error al actualizar el usuario. Código de respuesta: {response_patch.status_code}")
# Método post
new_post_data = {
    'userId': 1, 
    'title': 'Nuevo Post',
    'body': 'Contenido del nuevo post...'
}

response_post = requests.post(url='https://jsonplaceholder.typicode.com/posts',
                        json=new_post_data,
                        timeout=10)

if response_post.status_code == 201:
    print("Nuevo post creado correctamente")
else:
    print(f"Error al crear el post. Código de respuesta: {response_post.status_code}")
# Método delete
response_delete = requests.delete(url='https://jsonplaceholder.typicode.com/posts/1', timeout=10)

if response_delete.status_code == 200:
    print("Post eliminado correctamente")
else:
    print(f"Error al eliminar el post. Código de respuesta: {response_delete.status_code}")
