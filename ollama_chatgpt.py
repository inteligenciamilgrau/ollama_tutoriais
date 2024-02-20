from openai import OpenAI

client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1/")

response = client.chat.completions.create(
  model="llama2",
  messages=[
    {"role": "user", "content": "Qual a capital do Brasil?"},
  ]
)

print("Resposta:", response.choices[0].message.content)