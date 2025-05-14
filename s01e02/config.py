import os

from dotenv import load_dotenv


load_dotenv()

VERIFY_URL = os.getenv("VERIFY_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")