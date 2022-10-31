import speech_recognition as sr

class speech_listener():
    init_rec = None

    def __init__(self) -> None:
        self.init_rec = sr.Recognizer()

    def listen(self) -> str: 
        with sr.Microphone() as source:
            print("Let's speak!!")
            audio_data = self.init_rec.record(source, duration=5)
            print("Recognizing your text.............")
            text = self.init_rec.recognize_google(audio_data)
            print(text)
            return text

if __name__ == "__main__":
    s = speech_listener()

    while True:
        print(s.listen())