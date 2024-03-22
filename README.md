# slack-whisper-py

## Projektinitialisierung

Um das Projekt zu initialisieren, folgen Sie bitte den untenstehenden Schritten:

1. `python3 -m venv .venv`  

2. Aktivieren Sie die virtuelle Umgebung mit dem Befehl `source .venv/bin/activate`.

3. Installieren Sie die erforderlichen Pakete mit dem Befehl `pip install -U -r requirements.txt`.

Nachdem Sie diese Schritte abgeschlossen haben, ist das Projekt bereit zur Verwendung.

Readme zum compilen eines Whisper Models mit whisper.cpp: 
https://github.com/RUB-bschkuhl/slack-whisper-cpp/blob/master/README.md


Verwendung des kompilierten Models in /slack-whisper-cpp

Heruntergeladenes Model nach /slack-whisper-cpp/models verschieben, dann Nutzung über Terminal (Anleitung ebenfalls in der oben angegebenen Readme):
./main -m models/ggml-[model].bin -f samples/jfk.wav
Bspw. mit dem Whisper Medium Model
./main -m models/ggml-medium.bin -f samples/jfk.wav
