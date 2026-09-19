import os
import yaml

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from classes.refund_agent import Refund_Agent

azure_endpoint = os.getenv('AZURE_LLM_ENDPOINT')
model_deployment_name = os.getenv('LLM_MODEL_NAME')

with open ('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

credential = DefaultAzureCredential()
bearer_token = get_bearer_token_provider(credential, 'https://ai.azure.com/.default')
openai_client = OpenAI(
    base_url = azure_endpoint,
    api_key = bearer_token,
)

refund_agent = Refund_Agent(
    openai_client = openai_client,
    model_deployment_name = model_deployment_name,
    config = config
)

def process_message(user_message: str) -> str | None:
    return refund_agent.process_message(user_message)

def interactive_loop():
    print("Session has now started, enter 'quit' or 'exit' to end session.")

    while True:

        try:
            user_message = input('\nYou: ').strip()
        except (EOFError, KeyboardInterrupt):
            print('Exiting Session...')
            break

        if not user_message:
            continue
        if user_message.lower() in ('quit', 'exit'):
            print('Exiting Session...')
            break

        print("Processing user's message...")
        reply = refund_agent.process_message(user_message)

        if reply is None:
            print('Failed to get a response from model')
            continue
        
        print("\nRESPONSE:")
        print("=" * 50)
        print(reply)

if __name__ == '__main__':
    interactive_loop()

    


        
        
        

    
