from flask import Flask, request, jsonify, render_template
import tempfile
import os
from datetime import datetime
from pydub import AudioSegment
import requests
import subprocess


app = Flask(__name__)

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

# function to generate suggestions
@app.route("/generate-suggestions", methods=["POST"])
def generate_suggestions():
    # get prompt template and transcript
    prompt_template = request.form["prompt_template"]
    transcript = request.form["transcript"]
    prompt_template = "Generiere Fragen auf Basis des gesprochenen Textes."
    # generate suggestions
    suggestion = generate_suggestions(prompt_template, transcript)

    return jsonify({"suggestions": suggestion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)