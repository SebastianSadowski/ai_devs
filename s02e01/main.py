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
    loop = asyncio.get_event_loop()
    centrala = CentralaClient()
    ollama = OllamaEngine(model='hf.co/SpeakLeash/Bielik-4.5B-v3.0-Instruct-GGUF:latest')
    # ollama = OllamaEngine(model='SpeakLeash/bielik-11b-v2.2-instruct:Q4_K_M')
    gpt = AgentEngine(OPENAI_API_KEY)

    przesluchania_zip = centrala.get(['dane', 'przesluchania.zip']).content

    extract_to = 's02e01/przesluchania'
    if not os.listdir(extract_to):
        with zipfile.ZipFile(io.BytesIO(przesluchania_zip)) as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Pliki rozpakowane do folderu: {extract_to}")

    audio_files = list_audio_files(extract_to)
    print("Znalezione pliki audio:")


    files_in_path = list_files(extract_to)

    text_files = [ f for f in files_in_path if f.endswith(".m4ajson") ]
    print(text_files)

    if not text_files:
        promise_transcription = [
            loop.run_in_executor(None, read_audio_and_transcrypt, audio)
            for audio in audio_files
        ]
        transcryptions = loop.run_until_complete(asyncio.gather(*promise_transcription))

    else:
        transcryptions = [
            load_file(f)
            for f in text_files
        ]

    prompt_knowledge ="".join(
    f"zapis{i + 1}: {session}\n"
        for i, session in enumerate(transcryptions)
        )
    prompt = system_prompt(prompt_knowledge)
    print(prompt)

    resp = ollama.generate(prompt)
    # resp = ollama.generate("Adres to Nowa Iwiczna 12, daj znac co o nim wiesz")
    print(resp['response'])

    # before, after = resp.split('_answer', maxsplit=1)
    # after = resp["_answer"]
    # print("############################")
    # print("############answer:################")
    #
    #
    # prompt2 = f"""
    # Poniżej dostaniesz informacje o instytucie w którym wykładał profesor Maj, pobierz dane adresowe dla niego.
    #
    # RULES:
    # - Informacje mogą być szczątkowe, lub nie bezpośrednie
    # - śmiało myśl na głos a swoje myśli umieść w obiekcie _thoughts.
    # - wynik swojej analizy umieść w _conclusion
    # - adres, a dokładnie nazwę ulicy umieść w _answer
    # - w swojej analizie możesz wykorzystać mapy geolokalizacyjne takie jak Google Maps
    #
    # {after}
    # """
    #
    # print("############################")
    # print("############################")
    #
    # answer2 = gpt.generate(prompt2)
    #
    # print("############################")
    # print("############################")
    # print(answer2)
    #
    # centrala.post_answer(['report'], task_id="mp3", apikey=CENTRALA_KEY, payload="ul. prof. Stanisława Łojasiewicza 6")

