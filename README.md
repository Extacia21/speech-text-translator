# 🗣️ Text ↔ Speech Translator

A Flask-based web application that allows users to:
- Convert text to speech and download the result as an `.mp3` file
- Convert speech to text from audio uploads and download it as a `.docx` document

---

## 🔗 Live Demo

> Coming Soon (optional: add Netlify/Vercel/Fly.io deployment)

---

## 📸 Preview

| Text to Speech | Speech to Text |
|----------------|----------------|
| ![Text to Speech Screenshot](preview1.png) | ![Speech to Text Screenshot](preview2.png) |

---

## ✨ Features

- ✅ Text-to-Speech using `gTTS` (Google Text-to-Speech)
- ✅ Speech-to-Text using `SpeechRecognition` + Google API
- ✅ Upload and convert various audio formats (MP3, WAV, OGG, FLAC)
- ✅ Download results as `.mp3` or `.docx`
- ✅ Clean UI with two clear sections
- ✅ Unique output filenames to prevent overwriting
- ✅ Compatible with Windows, macOS, and Linux

---

## ⚙️ Technologies Used

- **Backend:** Flask (Python)
- **Text to Speech:** gTTS
- **Speech to Text:** SpeechRecognition + Google Speech API
- **Audio Processing:** pydub + FFmpeg
- **Document Generation:** python-docx
- **Frontend:** HTML + minimal styling

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-speech-translator.git
cd text-speech-translator
