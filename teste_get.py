import requests

headers = {'Authorization':'Token a08e5d3d8fa1a5c12707a959799967a9dbe8eb1a'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'

resultado = requests.get(url_base_cursos, headers=headers)

#print(resultado.json())

# Testando se o endpoint está correto

assert resultado.status_code == 200


#Testando a quantidade de registros

assert resultado.json()['count'] == 5


assert resultado.json()['results'][0]['titulo'] == "Programação com Java"