from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You area a helpful assistant."},
        {"role": "user", "content": "Vou viajar para Madrid em Setembro de 2024. Quero que faça um roteiro de viagem para mim"}
    ]
)

print(response.choices[0].message.content)