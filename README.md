### 📝 Voice-To-Text
A GUI-based voice-controlled notes application that allows users to dictate and save notes using **Vosk** (offline speech recognition) and **Tkinter** for GUI.  

## 🚀 Features  
✔️ **Voice-to-Text**: Convert speech into text notes.  
✔️ **Offline Support**: Uses **Vosk** for offline speech recognition.  
✔️ **Text-to-Speech (TTS)**: Read saved notes aloud using **pyttsx3**.  
✔️ **User-Friendly GUI**: Simple and intuitive interface with Tkinter.  
✔️ **Save & Load Notes**: Store and retrieve notes easily.  

## 📦 Installation  

### 1️⃣ **Install Dependencies**  
Run the following command to install the required libraries:  
```sh
pip install vosk pyaudio tkinter pyttsx3
```

### 2️⃣ **Download Vosk Model**  
Download an English model from:  
🔗 [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)  

For example:  
- **Small (~50MB, faster, less accurate)** → [Download](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip)  
- **Large (~1.8GB, more accurate)** → [Download](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip)  

**Extract & Rename:**  
- Unzip the downloaded file.  
- Rename the extracted folder to **"model"**.  
- Place it in the same directory as the Python script.  

### 3️⃣ **Run the Application**  
After setting up the model, run:  
```sh
python main.py
```

## 📌 File Structure  
```
/VoiceNotesApp
  ├── model/              <-- Vosk model folder
  ├── main.py             <-- Main Python script
  ├── requirements.txt    <-- Required dependencies
  ├── README.md           <-- Project documentation
```

## 🖥️ Usage  
1️⃣ Click the **"Start Recording"** button to dictate your note.  
2️⃣ The app will transcribe the speech into text.  
3️⃣ Click **"Save"** to store the note.  
4️⃣ Click **"Read Note"** to hear the note using TTS.  

## 🛠️ Troubleshooting  
- **Error: "No libpcap provider available" (Windows)**  
  → Install [Npcap](https://nmap.org/npcap/) for packet capturing.  
- **Microphone not detected?**  
  → Ensure that your microphone is properly connected and recognized.  

## 🔥 Future Enhancements  
✅ Add support for multiple languages.  
✅ Implement cloud storage for notes.  
✅ Enhance UI with more themes.  

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 💡 Author
👨‍💻 Developed by **Kunal Masurkar**  
🌐 [GitHub](https://github.com/kunal-masurkar) | 🔗 [LinkedIn](https://linkedin.com/in/kunal-masurkar-8494a123a)
