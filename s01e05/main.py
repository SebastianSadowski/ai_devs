from common.config import CENTRALA_KEY
from common.models.ollama_engine import OllamaEngine
from common.requests.centrala_client import CentralaClient


def system_prompt() -> str:
    return f"""
            You are a cryptographer and a specialist in data anonymization. 
            You are given a text and you need to anonymize it. You answer only in Polish language. 
            You anonymize first name and last name, city, street with number and age.
            Your goal is to return data in unchanged format and language, but anonymized. 
            Anonymization rules: You can use only 'CENZURA' word to anonymize.
            You anonymize first name and last name as one word, so you use CENZURA once.
            You anonymize city as one word, so you use CENZURA once
            You anonymize age as one word, so you use CENZURA once
            You anonymize street name and number as one word, so you use CENZURA once

        """


if __name__ == "__main__":
    centrala = CentralaClient()
    ollama_mistral = OllamaEngine()
    ollama_bielik = OllamaEngine(model = "SpeakLeash/bielik-11b-v2.2-instruct:Q4_K_M")


    fragile_data = centrala.get(['data', CENTRALA_KEY, 'cenzura.txt']).text
    print(fragile_data)

    resp = ollama_bielik.chat(system_prompt(), fragile_data, temperature=0.0)
    print(resp['message']['content'])

    final_resp = centrala.post_answer(['report'], task_id='CENZURA', apikey=CENTRALA_KEY, payload=resp['message']['content']).json()
    print(f'odpowiedź z centrali {final_resp}')