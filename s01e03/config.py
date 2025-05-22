import os

from dotenv import load_dotenv


load_dotenv()


_URL = os.getenv("url")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")