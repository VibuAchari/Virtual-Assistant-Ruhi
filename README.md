# Virtual Assistant: Ruhi

**Ruhi** is a voice-driven desktop assistant developed in Python. It provides offline interaction, text-to-speech responses, command history logging, and persistent data storage using MySQL. The application features a modern GUI with a dark glassmorphism design and is packaged to run independently on Windows systems.

---

## Features

- 🎤 Offline voice recognition using `speech_recognition`
- 🗣️ Text-to-speech responses via `pyttsx3`
- 🧠 Rule-based NLP classification
- 💾 Persistent command history stored in a **MySQL database**
- 📄 Exportable command logs in PDF format (`fpdf`)
- 🖥️ GUI built with `Tkinter` featuring a splash screen and dark theme
- 🧪 Built-in microphone testing utility
- 🔌 Fully offline, no cloud dependencies
- 📦 One-click `.exe` build support via PyInstaller

---

## Project Structure

```
Virtual-Assistant-Ruhi/
├── main.py                    # Entry point
├── ui/
│   ├── interface.py           # Main UI and interaction
│   ├── splash.py              # Splash screen window
│   └── test_mic.py            # Mic testing utility
├── core/
│   ├── voice.py               # Speech recognition & TTS
│   ├── logic.py               # Rule-based NLP classifier
│   └── database.py            # MySQL connection & logging
│   └── utils.py               # main functionalities
│   └── nlp.py                 #classification and command matching
│   └── media.py
│   └── pdfgen.py
│   └── wolfram.py             
├── resources/                 # UI assets (images/icons)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Requirements

- Python 3.8+
- MySQL Server running locally (or accessible remotely)
- Internet only for package installation (not required for runtime)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Virtual-Assistant-Ruhi.git
cd Virtual-Assistant-Ruhi
```

### Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate      # For Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## MySQL Setup

Create a MySQL database (e.g., `ruhi_assistant`) and update the credentials inside `core/database.py`:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="ruhi_assistant"
)
```

The assistant automatically creates a `history` table if it does not exist.

---

## Running the Assistant

```bash
python main.py
```

This will display the splash screen and then launch the main interface. Click the mic button to give voice commands.

---

## Testing the Microphone

```bash
python
>>> from core.voice import test_microphone
>>> test_microphone()
```

---

## Packaging into Executable (Windows)

Install PyInstaller:

```bash
pip install pyinstaller
```

Then build:

```bash
pyinstaller --noconfirm --onefile --windowed --add-data "resources;resources" main.py
```

Your executable will appear inside the `dist/` folder.

---

## .gitignore Recommendation

```gitignore
.venv/
__pycache__/
*.pyc
*.log
dist/
build/
*.spec
resources/history.pdf
```

---

## License

This project is licensed under the MIT License.

---

## Author

**Developer:** [@VibuAchari](https://github.com/VibuAchari)  

