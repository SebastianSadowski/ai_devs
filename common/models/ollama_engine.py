import argparse
import json

import requests


class OllamaEngine:
    def __init__(self, model: str = "mistral", base_url: str = "http://localhost:11434"):
        self.session = requests.session()
        self.base_url = base_url
        self.model = model



    def generate(self, prompt: str, temperature: float = 0.0) -> any:
        system_prompt = f"""
            You are a cryptographer and a specialist in data anonymization. 
            You are given a text and you need to anonymize it. You answer only in Polish language. 
            You anonymize first name and last name, city, street with number and age.
            Your goal is to return data in unchanged format and language, but anonymized. 
            Anonymization rules: You can use only 'CENZURA' word to anonymize.
            You anonymize first name and last name as one word, so you use CENZURA once.
            You anonymize city as one word, so you use CENZURA once
            You anonymize age as one word, so you use CENZURA once
            You anonymize street name and number as one word, so you use CENZURA once
        
        {prompt}
        """

        messages = [
                {"role": "system", "content": f"{system_prompt}"},
                {"role": "user", "content": f"{prompt}"}
        ]

        payload = {
            "model": self.model,
            "prompt": system_prompt,
            "stream": False,
            "temperature": temperature
        }


        try:
            response = self.session.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()

            response = json.loads(response.text)
            print(f"Total tokens: {len(response['context'])} or {response['prompt_eval_count'] + response['eval_count']}, prompt tokens: {response['prompt_eval_count']}, completion tokens: {response['eval_count']}")

        except Exception as e:
            print(f"Ollama error: {e}")
            return "N/A"

        return response

    def chat(self, prompt: str, temperature: float = 0.0) -> any:
        system_prompt = f"""
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

        messages = [
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{prompt}"}
        ]

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "temperature": temperature
        }

        try:
            response = self.session.post(f"{self.base_url}/api/chat", json=payload)
            response.raise_for_status()

            response = json.loads(response.text)
            print(
            f"Total tokens: {response['prompt_eval_count'] + response['eval_count']}, prompt tokens: {response['prompt_eval_count']}, completion tokens: {response['eval_count']}")

        except Exception as e:
            print(f"Ollama error: {e}")
            return "N/A"

        return response

