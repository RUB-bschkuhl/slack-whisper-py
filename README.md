# slack-whisper-py

## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Installation](#installation)
- [Benutzung](#benutzung)
- [Abhängigkeiten](#abhängigkeiten)
- [Beitragen](#beitragen)
- [Danksagungen](#danksagungen)
- [Lizenz](#lizenz)

## Einführung



## Installation

Um `slack-whisper-py` auf Ihrem Rechner zu installieren und einzurichten, folgen Sie diesen Schritten:

1. Stellen Sie sicher, dass Python 3 auf Ihrem System installiert ist.
2. Klonen Sie dieses Repository auf Ihren lokalen Rechner.
3. Navigieren Sie zum Projektverzeichnis und erstellen Sie eine virtuelle Umgebung:

    ```bash
    python3 -m venv .venv
    ```

4. Aktivieren Sie die virtuelle Umgebung:

    ```bash
    source .venv/bin/activate
    ```

5. Installieren Sie die erforderlichen Pakete:

    ```bash
    pip install -U -r requirements.txt
    ```

6. Fügen Sie eine `.env`-Datei hinzu, um Ihren OpenAI-API-Schlüssel zu hinterlegen:

    ```env
    OPENAI_API_KEY="Ihr_OpenAI_API_Schlüssel"
    ```

7. Befolgen Sie die Anweisungen, um das Whisper-Modell wie im [README von slack-whisper-cpp](https://github.com/RUB-bschkuhl/slack-whisper-cpp/blob/master/README.md) beschrieben zu kompilieren.

## Benutzung

Nach der Installation des Projekts und des Whisper-Modells, verschieben Sie das heruntergeladene Modell nach `/slack-whisper-cpp/models`. Um das kompilierte Modell zu verwenden, führen Sie den folgenden Befehl in Ihrem Terminal aus:

## Abhängigkeiten

`slack-whisper-py` benötigt folgende Abhängigkeiten:

- **Python 3**: [Installationsanleitung](https://www.python.org/downloads/)
- **Virtuelle Umgebung**: In Python 3 enthalten
- **Erforderliche Python-Pakete**: In `requirements.txt` aufgelistet
- **`slack-whisper-cpp` für die Kompilierung des Whisper-Modells**: [GitHub-Repository](https://github.com/RUB-bschkuhl/slack-whisper-cpp)

## Beitragen

Wir begrüßen Beiträge zum Projekt `slack-whisper-py`! Um beizutragen:

1. Forke das Repository.
2. Erstelle einen neuen Branch für dein Feature oder deinen Fix.
3. Committe deine Änderungen und pushe sie zu deinem Fork.
4. Reiche einen Pull Request mit einer klaren Beschreibung deiner Änderungen ein.

## Danksagungen

Ein besonderer Dank gilt den Beitragenden des `slack-whisper-cpp` Projekts für ihre Arbeit an der Kompilierung des Whisper-Modells. Ihr Projekt diente als Grundlage und Inspiration für `slack-whisper-py`.

Besonderer Dank geht auch an Alexander Mikasch ([Github](https://github.com/Freakrider)) und Annika Lambert für ihre Beiträge und Unterstützung des Projekts.
