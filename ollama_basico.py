#  verifica se ollama esta rodando: systemctl status ollama.service
import requests

print("Iniciando Assistente")

pergunta = "why is the sky blue?"

url = "http://localhost:11434/api/chat"
data = {
    "model": "llama2",
    "messages": [
        {"role": "user", "content": pergunta}
    ],
    "stream": False
}

response = requests.post(url, json=data)

print("Pergunta:", pergunta)
print("Se der 200 a resposta deu boa:", response.status_code)
print("Resposta:", response.json()['message']['content'])

print("Desligando")
