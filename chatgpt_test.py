import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "人間と音楽の関係性について教えてください"},
    ],
)
print(response.choices[0]["message"]["content"])