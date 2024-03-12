from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tempfile
import os
from datetime import datetime
from pydub import AudioSegment
import requests
import subprocess
from suggestions import generate_suggestions
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# render html
# TODO - Später Vue.js einbinden
@app.route("/")
def index():
    return render_template("index.html")

# function to transcript audio using whisper
@app.route("/process-audio", methods=["POST"])
def process_audio_data():
    # get audio file
    audio_file = request.files["audio"]
    # save audio file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ctype = audio_file.headers["Content-Type"]
    audio = requests.utils._parse_content_type_header(ctype)
    wav_file_path = '';
    txt_file_path = os.path.join(os.path.dirname(__file__), "Transcripts", f"{timestamp}_Transcript");
    if audio[0] == "audio/webm":
        # process webm file
        audio_file_path = os.path.join(os.path.dirname(__file__), "Audios", f"{timestamp}_Voice_Record.webm")
        audio_file.save(audio_file_path)
        webm_audio = AudioSegment.from_file(audio_file_path, format="webm")
        webm_audio = webm_audio.set_frame_rate(16000)  # Set the frame rate to 16000
        #webm_audio = webm_audio.split_to_mono()  # Set the frame rate to 16000
        webm_audio = webm_audio.set_channels(1)
        webm_audio = webm_audio.set_sample_width(2)
        # webm_audio = webm_audio.set_sample_rate(4)  # Set the frame rate to 16000
        wav_file_path = os.path.join(os.path.dirname(__file__), "Audios", f"{timestamp}_Voice_Record.wav")
        webm_audio.export(wav_file_path, format="wav")
        os.remove(audio_file_path)

        
    elif audio[0] == "audio/ogg":
        # process ogg file
        audio_file_path = os.path.join(os.path.dirname(__file__), "Audios", f"{timestamp}_Voice_Record.ogg")
        audio_file.save(audio_file_path)
        # convert ogg file to wav
        ogg_audio = AudioSegment.from_ogg(audio_file_path)
        ogg_audio = ogg_audio.set_frame_rate(16000)  # Set the frame rate to 16000
        ogg_audio = ogg_audio.set_channels(1)
        ogg_audio = ogg_audio.set_sample_width(2)  # Set the frame rate to 16000
        # ogg_audio = ogg_audio.set_sample_rate(4)  # Set the frame rate to 16000
        wav_file_path = os.path.join(os.path.dirname(__file__), "Audios", f"{timestamp}_Voice_Record.wav") 
        ogg_audio.export(wav_file_path, format="wav")
        os.remove(audio_file_path)
    else:
        # handle unsupported audio format
        return jsonify({"error": "Unsupported audio format. Only webm and mp3 files are allowed."})

    # TODO - Whisper
    # return transcript 
    result = subprocess.run(['../slack-whisper-cpp/main',
                            '-m',
                            '../slack-whisper-cpp/models/ggml-medium.bin',
                            '-f',
                            wav_file_path,
                            '--language',
                            'de',
                            '--translate',
                            'false',
                            '-otxt',
                            'true',
                            '-of',
                            txt_file_path
                            ], stdout=subprocess.PIPE)

    transcript = result.stdout.decode()

    #os.remove(wav_file_path)
    return jsonify({"transcript": transcript})

@app.route("/generate-suggestionsgpt3", methods=["POST"])
def generate_suggestions_endpoint3():
    # get prompt template and transcript
    data = request.get_json()
    prompt_template = data["prompt"]
    transcript = data["transcript"]
    
    # generate suggestions
    suggestions = generate_suggestions(prompt_template, transcript, gpt="gpt-3.5-turbo")
    
    return jsonify({"suggestions": suggestions})

@app.route("/generate-suggestionsgpt4", methods=["POST"])
def generate_suggestions_endpoint4():
    # get prompt template and transcript
    data = request.get_json()
    prompt_template = data["prompt"]
    transcript = data["transcript"]
    
    # generate suggestions
    suggestions = generate_suggestions(prompt_template, transcript, gpt="gpt-4-turbo-preview")
    return jsonify({"suggestions": suggestions})

@app.route("/searchandgenerate", methods=["POST"])
def suche_und_zusammenfassung():
    """
    Führt eine Suche durch und liefert eine Zusammenfassung der Ergebnisse zurück.
    
    :param query: Suchanfrage oder Transkript
    :param region: Region für die Suche (Standard ist "de-de")
    :param time: Zeitrahmen für die Suche (Standard ist "d" für Tag)
    :param max_results: Maximale Anzahl der Suchergebnisse
    :param backend: Spezifiziert das Backend, kann "news" für Nachrichtensuche sein
    :return: Zusammenfassung der Suchergebnisse
    """
    region="de-de"
    time="d"
    max_results=5
    backend=""
    data = request.get_json()
    transcript = data["transcript"]
    prompt_template = "Du bekommst ein Transkript. Erstelle dafür ein Suchschlagwort mit maximal 30 Zeichen."

    
    # generate suggestions
    query = generate_suggestions(prompt_template, transcript, gpt="gpt-3.5-turbo")
    print(query)
    # Anpassen des DuckDuckGoSearchAPIWrappers
    wrapper = DuckDuckGoSearchAPIWrapper(region=region, time=time, max_results=max_results)
    
    # Erstellen des Suchobjekts mit angepasstem Wrapper
    search = DuckDuckGoSearchResults(api_wrapper=wrapper)
    
    # Durchführung der Suche
    results = search.run(query)
    print(results)
    # Verarbeitung und Zusammenfassung der Ergebnisse
    # Diese Schritt wäre abhängig von den spezifischen Anforderungen und könnte so einfach oder komplex sein, wie benötigt.
    # Hier ein einfacher Ansatz, der die Titel der gefundenen Artikel zurückgibt:
    zusammenfassung = '\n'.join([f"Titel: {res['title']}, Link: {res['link']}" for res in results])
    
    return jsonify({"suggestions": zusammenfassung})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)