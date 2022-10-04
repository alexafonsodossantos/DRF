from mimetypes import add_type
import requests
from random import randint


class TesteCursos:
    headers = {"authorization": "Token 42dbe53bdd3e138d7e36ce42b8b0ecde3a5f3e8c"}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    test_id = 35

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200



    def test_post_curso(self):
        novo = {
            "titulo" : "curso de programação brainfuck sdfgsdfg",
            "url":f"http://asdfasdfassdfgdfsdfsd{randint(0,9999)}.com"
        }

        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201

        self.test_id = resposta.json()['id']




    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}{self.test_id}', headers=self.headers)
        assert curso.status_code == 200



    def test_put_curso(self):
        atualizado = {
            "titulo":"novo curso de luthiertuasdasdasuuuuuuu",
            "url":"http://asdfasdfassdfgdfsdfsdlkjljkljkl.com"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}{self.test_id}/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
    
    def test_put_titulocurso(self):
        atualizado = {
            "titulo":"novo curso de luthiertuasdasdasuuuuuuu",
            "url":"http://asdfasdfassdfgdfsdfsdlkjljkljkl.com"
        }


        resposta = requests.put(url=f'{self.url_base_cursos}{self.test_id}/', headers=self.headers)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def teste_delete_curso(self):
        resposta = requests.delete(f'{self.url_base_cursos}{self.test_id}', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
