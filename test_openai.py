import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    openai.models.list()
except Exception as e:
    print(f"Error: {e}")
