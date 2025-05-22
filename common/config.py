import os

from dotenv import load_dotenv

load_dotenv()


CENTRALA_KEY = os.getenv("CENTRALA_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LANGFUSE_PUBLIC_KEY = os.getenv("LANG_FUSE_PUB")
LANGFUSE_SECRET = os.getenv("LANG_FUSE_SECRET")
LANGFUSE_HOST = os.getenv("LANG_FUSE_HOST")