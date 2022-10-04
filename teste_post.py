import requests

headers = {'Authorization':'Token a08e5d3d8fa1a5c12707a959799967a9dbe8eb1a'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


novo_curso = {
    "titulo":"Curso de coach para galo de rinha",
    "url":"http://gasdglosdasdasdebrigabrabosasd.com",

}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

print(resultado.json()['id'])



# Testando o código de status HTTP

# assert resultado.status_code == 201

# Testando se o titulo do curso  retornado é o mesmo do informado

# assert resultado.json()['titulo'] == novo_curso['titulo']