# 🎙️ XTTS v2 Voice Cloning Project

A simple Python-based voice cloning system using **Coqui XTTS v2** for
multilingual text-to-speech generation.

This project allows you to generate speech using a reference voice
sample and a text script.

------------------------------------------------------------------------

## 🚀 Features

-   Multilingual voice cloning
-   Uses `xtts_v2` model
-   GPU acceleration (CUDA supported)
-   Script-based text input
-   Automatic memory cleanup after execution

------------------------------------------------------------------------

## 🧠 Model Used

Model: `tts_models/multilingual/multi-dataset/xtts_v2`\
Powered by Coqui TTS

------------------------------------------------------------------------

## 📦 Installation

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/WizenTree/voice-cloning-xtts.git
cd voice-cloning-xtts
```

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux / Mac)
source venv/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🎤 How to Use

### Step 1: Add Your Voice Sample

Place your reference voice file in the root folder and rename it to:

    my_sample_voice.wav

⚠️ Do NOT upload your personal voice file to GitHub.

------------------------------------------------------------------------

### Step 2: Add Script

Edit `script.txt` with the text you want spoken.

-   Lines starting with `#` will be ignored.
-   Maximum input length is 10,000 characters.

------------------------------------------------------------------------

### Step 3: Run the Script

``` bash
python main.py
```

Output file:

    final_recap_voice.wav

------------------------------------------------------------------------

## ⚡ First Run Warning

The first execution will download the XTTS model (\~1GB).\
Subsequent runs will be significantly faster.

------------------------------------------------------------------------

## 🖥️ GPU Support

The script automatically detects CUDA:

``` python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

------------------------------------------------------------------------

## 🧹 Memory Cleanup

After execution, the script:

-   Deletes model instance
-   Clears CUDA cache
-   Runs garbage collection

------------------------------------------------------------------------

## 📁 Recommended Project Structure

    voice-cloning-xtts/
    │
    ├── voice_clone.py
    ├── requirements.txt
    ├── script.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## 📌 Notes

-   Voice quality improves with 10--30 seconds of clean reference audio.
-   For long scripts, consider splitting text into smaller chunks.
-   Ensure your system has sufficient RAM/VRAM for best performance.

------------------------------------------------------------------------

## 🔮 Future Improvements Maybe

-   Batch audio generation
-   Streamlit web interface
-   FastAPI REST API
-   Docker containerization
-   Emotion control support

------------------------------------------------------------------------

## 📜 License

This project uses Coqui TTS. Please follow their official license
guidelines.

------------------------------------------------------------------------

## 👨‍💻 Author

Built as part of AI experimentation and voice cloning research.
