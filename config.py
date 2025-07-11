import os
from dotenv import load_dotenv

load_dotenv()

USE_AZURE = True

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Optional fallback
MODEL = "gpt-4o"
TEMPERATURE = 0
