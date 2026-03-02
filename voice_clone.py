import os
import torch
import gc
import sys
from TTS.api import TTS

# --- CONFIGURATION ---
REFERENCE_VOICE = "my_sample_voice.wav" 
INPUT_SCRIPT = "script.txt"
OUTPUT_AUDIO = "final_recap_voice.wav"

def run_voice_cloning():
    print("\n[1/3] Initializing XTTS Engine...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    try:
        tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        ).to(device)
        
        tts.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

        if not os.path.exists(INPUT_SCRIPT):
            print(f"❌ Error: {INPUT_SCRIPT} not found!")
            return
            
        with open(INPUT_SCRIPT, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if not l.startswith("#") and l.strip()]
        
        full_text = " ".join(lines)
        
        print(f"\n[2/3] Model Loaded. Generating audio for {len(full_text)} characters...")
        print("--- Note: The first run takes longer as it caches the model ---")
        
        # 3. Generate the Clone
        tts.tts_to_file(
            text=full_text[:10000], 
            speaker_wav=REFERENCE_VOICE,
            language="en",
            file_path=OUTPUT_AUDIO
        )
        
        print(f"\n[3/3] ✅ SUCCESS: Created {OUTPUT_AUDIO}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
    
    finally:
        if 'tts' in locals():
            del tts
        gc.collect()
        torch.cuda.empty_cache()

if __name__ == "__main__":
    # Check for the voice sample first!
    if not os.path.exists(REFERENCE_VOICE):
        print(f"❌ STOP: You need to put a file named '{REFERENCE_VOICE}' in this folder.")
        sys.exit()
        
    run_voice_cloning()