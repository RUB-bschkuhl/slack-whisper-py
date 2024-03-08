from flask import Flask, request, jsonify, render_template
import tempfile
import os
from datetime import datetime

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
    audio_file_path = os.path.join(os.path.dirname(__file__), "Audios", f"{timestamp}_Voice_Record.wav")
    audio_file.save(audio_file_path)
    
    # TODO - Whisper
    # return transcript
    return jsonify({"transcript": "Hello World"})

# function to generate suggestions
@app.route("/generate-suggestions", methods=["POST"])
def generate_suggestions():
    return jsonify({"suggestions": ["Hello", "World"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)