import requests

headers = {'Authorization':'Token 42dbe53bdd3e138d7e36ce42b8b0ecde3a5f3e8c'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


curso_atualizado = {
    "titulo":"Novo curso de SCRUM 3",
    "url":"http://cursocurso.com",
}

# buscando curso id 6

#curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
#print(curso.json())

resultado = requests.put(url =f' {url_base_cursos}6/', headers=headers, data=curso_atualizado)

# testa o codigo de status HTTP

assert resultado.status_code == 200

# Testando o titlo

assert resultado.json()['titulo'] == curso_atualizado['titulo']

print(resultado.json()['titulo'])