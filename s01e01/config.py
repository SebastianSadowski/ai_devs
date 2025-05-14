import os
from dotenv import load_dotenv

load_dotenv()

LOGIN_URL = os.getenv("LOGIN_URL")
USERNAME = os.getenv("XYZ_USERNAME")
PASSWORD = os.getenv("XYZ_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print(LOGIN_URL, USERNAME, PASSWORD, OPENAI_API_KEY)