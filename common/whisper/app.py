import uvicorn
from fastapi import FastAPI, File, UploadFile
import whisper
import tempfile

app = FastAPI()

# 🔁 Ładujemy model tylko raz!
model = whisper.load_model("medium")

if __name__ == "__main__":
    uvicorn.run(
        "common.whisper.app:app",  # ścieżka do Twojej aplikacji
        host="127.0.0.1",          # lub np. "0.0.0.0" by było dostępne z zewnątrz
        port=8001,
        reload=True,              # hot-reload przy zmianie pliku
        workers=1,                # liczba procesów (jeśli masz wiele CPU)
        log_level="info"
    )

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Zapisz plik tymczasowo
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Transkrybuj
    result = model.transcribe(tmp_path)
    return {"transcription": result["text"]}