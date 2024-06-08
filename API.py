"""Desarrollo del punto 3"""

import requests
url='https://my-json-server.typicode.com/Stiven1999A/Actividad_PI/db.json'
response = requests.post(url, timeout=10)
data = response.json()
print(data)
requests.post(
    url='https://my-json-server.typicode.com/Stiven1999A/Programacion_Para_La_Industria/posts',
    data={'title': 'foo',
          'body': 'bar',
          'userId': 1,
          },
    timeout=10)

requests.put(
    url='https://my-json-server.typicode.com/Stiven1999A/Programacion_Para_La_Industria/posts/1',
    data={
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
    },
    timeout=10)
