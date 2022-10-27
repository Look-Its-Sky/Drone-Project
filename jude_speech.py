import speech_recognition as sr
import pyaudio

class speech_listener():
    init_rec = None

    def __init__(self) -> None:
        self.init_rec = sr.Recognizer()

    def listen() -> str: 
        with sr.Microphone() as source:
            print("Let's speak!!")
            audio_data = init_rec.record(source, duration=5)
            print("Recognizing your text.............")
            text = init_rec.recognize_google(audio_data)
            return text