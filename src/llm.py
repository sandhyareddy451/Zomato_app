from groq import Groq
from src.prompt import system_instruction

client = Groq()

messages = [{"role": "system", "content": system_instruction}]

def ask_order (messages, model = "openai/gpt-oss-20b", temperature=0):
    response = client.chat.completions.create(
    model=model,
    messages = messages,
    temperature = temperature
    )
    return response.choices[0].message.content
    
    