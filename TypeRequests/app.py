import requests
import json

def get_api():
    url = ""
    resposta = requests.get(url)

    dados = resposta.json()

    print("Nome:", dados['name'])
    print("Email:", dados['email'])
    print("Cidade:", dados['address']['city'])

    print(json.dumps(dados, indent=4))

def post_api():
    dados = {'nome': 'will', 'idade': 20}
    res = requests.post('https://httpbin.org/post', json=dados)
    print(res.json())
 
def busca():
    params = {'busca': 'python'}
    res = requests.get('https://jsonplaceholder.typicode.com/users/1', params=params)
    print(res.url)
  
    