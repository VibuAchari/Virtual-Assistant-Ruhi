# core/voice.py

import pyttsx3
import speech_recognition as sr
import os


# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 2.0)


def speak(text):
    print(f"Ruhi: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    mic_index = 0

    try:
        mic_names = sr.Microphone.list_microphone_names()
        for i, name in enumerate(mic_names):
            if "mic" in name.lower() or "input" in name.lower():
                mic_index = i
                break

        with sr.Microphone(device_index=mic_index) as source:
            print(f"🎤 Using: {mic_names[mic_index]}")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            query = recognizer.recognize_google(audio, language="en-IN")
            print(f"You: {query}")
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Speech service unavailable.")
            return None

    except OSError as e:
        print(f"Microphone error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in voice.listen(): {e}")
        return None


def test_microphone():
    recognizer = sr.Recognizer()
    mic_names = sr.Microphone.list_microphone_names()

    print("🔍 Detected microphones:")
    for i, name in enumerate(mic_names):
        print(f"[{i}] {name}")

    try:
        index = int(input("🎤 Choose device index to test: "))
        with sr.Microphone(device_index=index) as source:
            print(f"\n🎧 Listening using: {mic_names[index]}")
            recognizer.adjust_for_ambient_noise(source)
            print("🎙️ Speak something...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            query = recognizer.recognize_google(audio, language="en-IN")
            print(f"🧠 Recognized: {query}")
            speak(f"You said: {query}")
        except sr.UnknownValueError:
            print("🤷 Couldn't understand the audio.")
        except sr.RequestError:
            print("❌ Could not reach speech recognition service.")

    except Exception as e:
        print(f"💥 Error during mic test: {e}")
