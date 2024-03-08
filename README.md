# slack-whisper-py

## Projektinitialisierung

Um das Projekt zu initialisieren, folgen Sie bitte den untenstehenden Schritten:

1. `python3 -m venv .venv`  

2. Aktivieren Sie die virtuelle Umgebung mit dem Befehl `source .venv/bin/activate`.

3. Installieren Sie die erforderlichen Pakete mit dem Befehl `pip install -U -r requirements.txt`.

Nachdem Sie diese Schritte abgeschlossen haben, ist das Projekt bereit zur Verwendung.



Verwendung des für AEN kompilierten Models in /slack-whisper-cpp

Model aus Sciebo nach /slack-whisper-cpp/models verschieben dann:
./main -m models/ggml-[model].bin -f samples/jfk.wav
E.g. mit dem Whisper Medium Model
./main -m models/ggml-medium.bin -f samples/jfk.wav
