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
        
        {prompt}
        """
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




if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Wykonaj inferencję z modelem Ollama")
        parser.add_argument("prompt", type=str, help="Tekst wejściowy (prompt)")
        parser.add_argument("--model", type=str, default="mistral", help="Nazwa modelu (domyślnie: mistral)")
        parser.add_argument("--stream", action="store_true", default=False,
                            help="Czy używać streamowania (strumieniowania odpowiedzi)")

        args = parser.parse_args()
        print(args)
        result = generate_response(args.model, args.prompt, args.stream)
        if result:
            print(result)