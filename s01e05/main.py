from common.config import CENTRALA_KEY
from common.models.ollama_engine import OllamaEngine
from common.requests.centrala_client import CentralaClient

if __name__ == "__main__":
    centrala = CentralaClient()
    ollama_mistral = OllamaEngine()
    ollama_bielik = OllamaEngine(model = "SpeakLeash/bielik-11b-v2.2-instruct:Q4_K_M")


    fragile_data = centrala.get(['data', CENTRALA_KEY, 'cenzura.txt']).text
    print(fragile_data)

    resp = ollama_bielik.chat(fragile_data, temperature=0.0)
    print(resp['message']['content'])

    final_resp = centrala.post_answer(['report'], task_id='CENZURA', apikey=CENTRALA_KEY, payload=resp['message']['content']).json()
    print(f'odpowiedź z centrali {final_resp}')