import speech_recognition as sr


class Listener:
    """Handles microphone input and speech recognition."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("\nListening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            except sr.WaitTimeoutError:
                print("No voice detected.")
                return ""

        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio)

            print(f"You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("Voice not clear.")
            return ""

        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return ""