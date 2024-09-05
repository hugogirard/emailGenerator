from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import os

class OpenAI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAI, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
          load_dotenv()
          self.chat = AzureChatOpenAI(
              azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
              azure_deployment=os.getenv('AZURE_OPENAI_DEPLOYMENT'),
              azure_api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
              azure_key=os.getenv('AZURE_OPENAI_KEY')
          )          