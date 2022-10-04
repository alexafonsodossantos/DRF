import requests

headers = {'Authorization':'Token 42dbe53bdd3e138d7e36ce42b8b0ecde3a5f3e8c'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o status HTTP

assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é 0

assert len(resultado.text) == 0