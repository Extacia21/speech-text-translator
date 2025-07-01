import os
import uuid
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from gtts import gTTS
import speech_recognition as sr
from docx import Document
from pydub import AudioSegment

app = Flask(__name__)
app.secret_key = 'secret'  # Needed for flashing messages

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Ensure ffmpeg is set for pydub
AudioSegment.converter = "ffmpeg"  # Optional if ffmpeg is in PATH


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form.get('text')
    lang = request.form.get('lang', 'en')

    if not text or not text.strip():
        flash("Please provide text input.")
        return redirect(url_for('index'))

    try:
        tts = gTTS(text=text, lang=lang)
        audio_filename = f"output_{uuid.uuid4().hex}.mp3"
        audio_path = os.path.join(OUTPUT_FOLDER, audio_filename)
        tts.save(audio_path)

        return send_file(audio_path, as_attachment=True)
    except Exception as e:
        flash(f"Error generating audio: {str(e)}")
        return redirect(url_for('index'))


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files.get('audio')

    if not audio_file:
        flash("No audio file provided.")
        return redirect(url_for('index'))

    try:
        original_filename = os.path.join(UPLOAD_FOLDER, audio_file.filename)
        audio_file.save(original_filename)

        # Convert to WAV if needed
        ext = os.path.splitext(original_filename)[-1].lower()
        if ext != '.wav':
            converted_filename = os.path.splitext(original_filename)[0] + ".wav"
            audio = AudioSegment.from_file(original_filename)
            audio.export(converted_filename, format="wav")
        else:
            converted_filename = original_filename

        # Transcribe with SpeechRecognition
        r = sr.Recognizer()
        with sr.AudioFile(converted_filename) as source:
            audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Speech could not be understood."
        except sr.RequestError:
            text = "Google API unavailable or quota exceeded."

        # Save to DOCX
        doc = Document()
        doc.add_paragraph(text)
        doc_filename = f"transcription_{uuid.uuid4().hex}.docx"
        doc_path = os.path.join(OUTPUT_FOLDER, doc_filename)
        doc.save(doc_path)

        return send_file(doc_path, as_attachment=True)

    except Exception as e:
        flash(f"Error processing audio file: {str(e)}")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
