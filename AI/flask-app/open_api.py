from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="write a flask app that uses Open API keys to be used in another UI."
)

print(response.output_text)
