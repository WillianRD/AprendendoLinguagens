import requests

def getApi():
    url = "https://api.ai-cats.net/v1/cat"

    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            try:
                data = response.json()
                print("JSON:", data)
                return data
            except ValueError:
                print("Erro: A resposta não está em formato JSON.")
                print("Conteúdo bruto:", response.text)
                return None
        else:
            print("Erro: A API retornou um status inesperado.")
            print("Conteúdo:", response.text)
            return None

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None

getApi()
