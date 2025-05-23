from common.models.ollama_engine import OllamaEngine

if __name__ == "__main__":
    ollama = OllamaEngine()

    resp = ollama.generate("hi, how you doing? who you are?", temperature=2.0)
    print(resp['response'])