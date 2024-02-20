import requests

print("Ativando assistente")

def perguntar(questao):
    url = "http://localhost:11434/api/chat"
    data = {
        "model": "llama2",
        "messages": [
            {"role": "user", "content": questao}
        ],
        "stream": False
    }

    return requests.post(url, json=data)

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        break

    resposta = perguntar(pergunta)
    # print("Se der 200 a resposta deu boa:", resposta.status_code)
    print(resposta.json()['model'] + ":", resposta.json()['message']['content'])

print("Desligando")
