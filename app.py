from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Default Gujarati Diwali message
    default_gujarati_text = (
        "સુખ અને સમૃદ્ધિ તમારા આંગણામાં ચમકે… "
        "દીવા શાંતિના ચારેય દિશાઓમાં ઝળકે… "
        "ખુશીઓ તમારા ઘર આંગણે આવીને ઉજવણી કરે… "
        "દિવાળીના તહેવારની તમને હાર્દિક શુભકામનાઓ!!"
    )
    return render_template('index.html', default_gujarati_text=default_gujarati_text)

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    name = request.form.get('name', '').strip()
    default_text = request.form.get('default_text', '')

    # Combine name with message if provided
    gujarati_text = f"{name}, {default_text}" if name else default_text

    # Convert text to speech and save in a BytesIO object
    mp3_fp = BytesIO()
    tts = gTTS(text=gujarati_text, lang='gu')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # Reset pointer to start of file

    # Save the audio to a temporary file
    audio_file_path = "static/diwali_greeting.mp3"
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(mp3_fp.read())

    return jsonify({'audio_url': audio_file_path})

if __name__ == '__main__':
    app.run(debug=True)
