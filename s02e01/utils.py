import json
import os
import base64
from typing import NamedTuple

import requests
from urllib.error import HTTPError

class Transcription(NamedTuple):
    path: str
    content: str

def read_audio_and_transcrypt(file_path: str) -> str:
    print(f"{file_path} transcription started!")
    try:
        with open(file_path, "rb") as file:
            audio = {
                "file": ("plik.mp3", file, "audio/mpeg")
            }
            resp = requests.post("http://localhost:8000/transcribe", files=audio).text
        print(f"{file_path} transcription done!")
        t = Transcription(file_path + ".json", json.loads(resp)["transcription"])
        save_file(t)
        return t.content

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def list_audio_files(folder_path: str):
    audio_extensions = (".mp3", ".wav", ".m4a", ".flac", ".ogg")
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(audio_extensions)
    ]

def list_files(folder_path: str):
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
    ]

def load_file(file: str)-> str:
    with open(file, "r") as f:
        return f.read()

def mp3_to_base64_string(file: str) -> str:
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def save_file(file:Transcription):
    print(f"saving file: {file.path} ")
    with open(file.path, "w") as f:
        f.write(file.content)
    print("saving done")


def system_prompt(context: str) -> str:
    return f"""
    ROLE: 
        Jesteś detektywem, który na podstawie przesłuchań musi ustalić fakty. 
        
    GOAL:
        Twoim celem jest ustalenie konretnej lokalizacji, a przynajmniej ulicy, przy której znajduie się instytut, na podstawie otrzymanych transkrypcji. Szukasz instytutu w którym wykładał profesor Maj
    
    CONTEXT: 
        Dostaniesz transkrypcję przesłuchań, niektórzy uczestnicy mogli być zestresowani, niewyraźnie się wypowiadać, musisz mieć na uwadzę, że niektóre słowa mogły być źłe przetłumaczone.
        Nie każdy przesłuchiwany wiedział o co był pytany, a pod presją mógł kłamać, miej na uwadzę, że niektóre wypowiedzi mogą być błędne.
        
        
   RULES:
    - Każdą z rozmów przeanalizuj osobno, nastepnie wszystkie przeanalizuj razme.
    - Stwórz strukturę listy
    - w liscie beda obiekty z nastepujacymi sekcjami: _zapisNr, _thoughts, _conclusion 
    - ostatni obiekt na liscie bedzie mial pola _final_thoughts, _answer
    - WYPISZ swoje przemyslenia w polu _final_thoughts przed ostateczna odpowiedzia _answer
    - MYŚL NA GŁOS, swoje przemyślenia możesz umieszczać w sekcji: _thoughts, 
    - ODPOWIEDŻ umieść w polu _conclusion, zawsze umieść konkluzje
    - JESLI nie podal nikt ulicy, sprobuj sam poszukac informacji o ulicy dla wskazanego miejsca w sieci, nie ograniczaj sie tutaj do podanych informacji
    - swoja finalna odpowiedz umiesc w klauzuli _answer: na koncu wypowiedzi 
    - pamiętaj, że w przesłuchaniach padają nazwy ulic, ale onie napewno nie są miejscem które suzkasz.
    
    JAK MYŚLEĆ:
     Pamiętaj aby myśleć na głos, w swoich myślach uwzględnij takie rzeczy jak: 
     - czy jest podany adres, czy to jest adres do tego miejsca
     - czy osoba ma wątpliwości
     - czy to adres osoby powiązanej z pytaniem
     - jakie emocje wyrażała osoba
     - czy osoba była pewna siebie
     
    
    
    KNOWLEDGE:
     {context}
    
    
    
    """