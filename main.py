import ollama
import asyncio
from ollama import AsyncClient
from ollama import Client

model = 'AISA'
messages = []
# Roles
USER = 'user'
ASSISTANT = 'assistant'

def add_history(content, role):
    messages.append({'role': role, 'content': content})

async def chat(message):
    add_history(message, USER)
    async for each_response in await AsyncClient().chat(model=model, messages=messages, stream=True):
      complete_message = ''
      complete_message += each_response['message']['content']
      print(each_response['message']['content'], end='', flush=True)
    add_history(complete_message, ASSISTANT)

def main():
  while True:
      print('\nQ to quit')
      prompt = input('Enter your message: ')
      if prompt.lower() == 'q':
          break
      else:
          asyncio.run(chat(prompt))
          print("\n")
          print("------------------------------------------------")

if __name__ == "__main__":
   main()
