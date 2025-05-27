import asyncio
import io
import json
import os
import zipfile

import requests

from common.config import OPENAI_API_KEY, CENTRALA_KEY
from common.models.agent_engine import AgentEngine
from common.models.ollama_engine import OllamaEngine
from common.requests.centrala_client import CentralaClient
from s02e01.utils import list_files, read_audio_and_transcrypt, list_audio_files, system_prompt, load_file

if __name__ == "__main__":
    ollama = OllamaEngine(model='hf.co/SpeakLeash/Bielik-4.5B-v3.0-Instruct-GGUF:latest')
    resp = ollama.generate("siemka, jak tam", temperature=2.0)
    print(resp)