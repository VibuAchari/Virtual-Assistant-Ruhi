# Virtual-Assistant-Ruhi
# 🤖 Ruhi – Your Personal Virtual Assistant (Web Edition)

**Ruhi** is a fully modular, voice-powered virtual assistant rebuilt with a modern web interface using **Flask**, **MySQL**, **Tailwind CSS**, and **pure Python logic** (no AI).  
She can handle your queries, track command history, open apps/websites, tell jokes, summarize Wikipedia results, do math, and more — all from a slick browser interface. ✨

---

## 📂 Project Structure

```
ruhi-assistant/
├── app.py
├── config.py
├── requirements.txt
│
├── assistant/
│   ├── __init__.py
│   ├── core.py
│   ├── tts.py
│   └── recognizer.py
│
├── database/
│   ├── __init__.py
│   └── mysql_handler.py
│
├── static/
│   └── css/
│       └── tailwind.css (optional if using CDN)
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
```

---

## 🚀 Features

✅ Voice-controlled assistant (mic input using browser speech API)  
✅ Flask-powered web UI with Tailwind CSS  
✅ User login & signup with MySQL authentication  
✅ Command history (stored + downloadable PDF)  
✅ Response output via text and speech (using `pyttsx3`)  
✅ Math calculations, jokes, Wikipedia summaries  
✅ Battery checks, recent query tracking, and more

---

## 💠 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ruhi-assistant.git
cd ruhi-assistant
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Configure Database

Make sure you have MySQL running. Then open `config.py` and set your credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'ruhidb'
}
```

✅ Ruhi will auto-create the necessary tables on first run.

---

## 🔊 How to Run

```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🎙️ Browser Voice Input

Click the 🎧 mic icon next to the input box — your browser will convert speech to text using the Web Speech API and Ruhi will take care of the rest!

---

## 🔐 Login Credentials

You can create a new user via `/signup`. Ruhi uses MySQL to persist user details and query history.

---

## 📸 Screenshots

| Login Page                         | Dashboard with Commands             |
|-----------------------------------|-------------------------------------|
| ![login](assets/login.png)        | ![dashboard](assets/dashboard.png) |

> Add actual screenshot links when you upload the images to your repo.

---

## 👨‍💻 Built With

- [Flask](https://flask.palletsprojects.com/)
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
- [Tailwind CSS](https://tailwindcss.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [Plyer](https://pypi.org/project/plyer/)

---

## 🙌 Credits

Created with 💙 by **[Vibusha S Achari]**  


---

## 📜 License

MIT License — Use it, remix it, rule with it.

