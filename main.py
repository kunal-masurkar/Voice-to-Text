import tkinter as tk
from tkinter import scrolledtext
import vosk
import pyttsx3
import pyaudio
import json

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Initialize speech recognition model
model = vosk.Model("model")  # place the dir properly
recognizer = vosk.KaldiRecognizer(model, 16000)

# Audio input setup
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def recognize_speech():
    """Captures and transcribes voice input."""
    text = ""
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            break
    return text

def add_note():
    """Adds recognized speech as a note."""
    note = recognize_speech()
    if note:
        text_area.insert(tk.END, note + "\n")

def read_notes():
    """Reads out loud the notes using TTS."""
    notes = text_area.get("1.0", tk.END).strip()
    if notes:
        engine.say(notes)
        engine.runAndWait()

def save_notes():
    """Saves notes to a file."""
    with open("notes.txt", "w") as file:
        file.write(text_area.get("1.0", tk.END))

# GUI setup
root = tk.Tk()
root.title("Voice-Controlled Notes App")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

text_area = scrolledtext.ScrolledText(root, width=50, height=15, font=("Arial", 12))
text_area.pack(pady=10)

btn_add = tk.Button(root, text="Add Note (Voice)", command=add_note, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_add.pack(pady=5)

btn_read = tk.Button(root, text="Read Notes", command=read_notes, bg="#2196F3", fg="white", font=("Arial", 12))
btn_read.pack(pady=5)

btn_save = tk.Button(root, text="Save Notes", command=save_notes, bg="#FF9800", fg="white", font=("Arial", 12))
btn_save.pack(pady=5)

root.mainloop()
