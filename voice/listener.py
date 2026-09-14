import speech_recognition as sr


class Listener:
    """Handles wake-word detection and speech recognition."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.wake_words = [
            "hey jarvis",
            "hello jarvis",
            "jarvis"
        ]

    def listen_once(self, phrase_time_limit=5):
        """
        Listen to one short voice input and convert it to text.
        """

        with sr.Microphone() as source:
            print("\nListening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=phrase_time_limit
                )

            except sr.WaitTimeoutError:
                print("No voice detected.")
                return ""

        try:
            print("Recognizing...")

            command = self.recognizer.recognize_google(
                audio
            )

            command = command.lower().strip()

            print(f"You said: {command}")

            return command

        except sr.UnknownValueError:
            print("Voice not clear.")
            return ""

        except sr.RequestError:
            print(
                "Speech recognition service is unavailable."
            )
            return ""

    def listen_for_wake_word(self):
        """
        Wait until the user says Hey JARVIS.
        """

        command = self.listen_once(
            phrase_time_limit=4
        )

        if not command:
            return False

        for wake_word in self.wake_words:
            if wake_word in command:
                print("Wake word detected.")
                return True

        print("Wake word not detected.")
        return False

    def listen_for_command(self):
        """
        Listen for the actual command after wake word detection.
        """

        print("Yes sir. What can I do for you?")

        return self.listen_once(
            phrase_time_limit=8
        )

    def listen(self):
        """
        Compatibility method for the existing app.py.

        It waits for Hey JARVIS, then captures the command.
        """

        wake_detected = self.listen_for_wake_word()

        if not wake_detected:
            return ""

        return self.listen_for_command()