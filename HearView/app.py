import whisper
import pyautogui
import time
import sounddevice as sd
import numpy as np
import wave

# Load Whisper model
model = whisper.load_model("base")  # Options: "tiny", "base", "small", "medium", "large"

# Function to type and send text into Tinkercad
def send_to_tinkercad(text):
    pyautogui.typewrite(text)
    pyautogui.press("enter")

# Function to record audio and save it as a WAV file
def record_audio(filename="speech.wav", duration=5, samplerate=16000):
    print("Recording... Speak now!")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()  # Wait for the recording to complete
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

# Notify user to switch to Tinkercad
print("Switch to the Tinkercad Serial Monitor NOW and leave it open.")
time.sleep(5)  # Give time to switch to Tinkercad

while True:
    # Record audio and save as "speech.wav"
    record_audio()

    # Transcribe audio using Whisper
    print("Transcribing...")
    result = model.transcribe("speech.wav")
    text = result["text"]

    print(f"Recognized: {text}")

    # Send transcribed text to Tinkercad Serial Monitor
    send_to_tinkercad(text)
