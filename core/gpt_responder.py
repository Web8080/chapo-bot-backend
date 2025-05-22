import openai
from config.keys import OPENAI_API_KEY
from config.settings import DEFAULT_MODEL, TEMPERATURE

openai.api_key = OPENAI_API_KEY

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE
    )
    return response.choices[0].message["content"].strip()
