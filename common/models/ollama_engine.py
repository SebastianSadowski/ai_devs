import argparse
import json
import time

import requests


class OllamaEngine:
    def __init__(self, model: str = "mistral", base_url: str = "http://localhost:11434"):
        self.session = requests.session()
        self.base_url = base_url
        self.model = model



    def generate(self, prompt: str, temperature: float = 0.0) -> any:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "temperature": temperature
        }


        try:
            start = time.perf_counter()
            response = self.session.post(f"{self.base_url}/api/generate", json=payload)


            end = time.perf_counter()
            print(f"Czas wykonania promptu {self.model}: {end - start:.6f} s")
            response.raise_for_status()

            response = json.loads(response.text)
            print(f"Total tokens: {len(response['context'])} or {response['prompt_eval_count'] + response['eval_count']}, prompt tokens: {response['prompt_eval_count']}, completion tokens: {response['eval_count']}")

        except Exception as e:
            print(f"Ollama error: {e}")
            return "N/A"

        return response

    def chat(self, system_prompt:str, prompt: str, temperature: float = 0.0) -> any:
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
            start = time.perf_counter()
            response = self.session.post(f"{self.base_url}/api/chat", json=payload)

            end = time.perf_counter()
            print(f"Czas wykonania promptu {self.model}: {end - start:.6f} s")
            response.raise_for_status()

            response = json.loads(response.text)
            print(
            f"Total tokens: {response['prompt_eval_count'] + response['eval_count']}, prompt tokens: {response['prompt_eval_count']}, completion tokens: {response['eval_count']}")

        except Exception as e:
            print(f"Ollama error: {e}")
            return "N/A"

        return response

