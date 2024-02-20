from ollama import Client  # pip install ollama

client = Client(host='http://localhost:11434')
model = "llama2"

print("Ativando assistente")

def perguntar(questao):
    stream = client.chat(model=model, stream=True, messages=[{'role': 'user', 'content': questao}])
    return stream

while True:
    perguntando = input("Você: ")
    if perguntando.lower() == "sair":
        break

    resposta = perguntar(perguntando)
    print(model + ": ", end="")
    for chunk in resposta:
        print(chunk['message']['content'], end='', flush=True)
    print("")


print("Desligando")
