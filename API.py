import requests as rq

rq.post(url='https://my-json-server.typicode.com/Stiven1999A/Programacion_Para_La_Industria/posts',data={
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  })