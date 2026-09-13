import pyttsx3
import threading


class Speaker:
    """Reliable Windows voice output for J.A.R.V.I.S."""

    def __init__(self, rate=165, volume=1.0):
        self.rate = rate
        self.volume = volume

        # Prevent two voice outputs from speaking together
        self.voice_lock = threading.Lock()

    def speak(self, text):
        """Speak every response using a fresh voice engine."""

        if not text:
            return

        text = str(text)

        print(f"JARVIS: {text}")

        with self.voice_lock:
            engine = None

            try:
                # Create a fresh engine for every response
                engine = pyttsx3.init("sapi5")

                engine.setProperty(
                    "rate",
                    self.rate
                )

                engine.setProperty(
                    "volume",
                    self.volume
                )

                voices = engine.getProperty(
                    "voices"
                )

                if voices:
                    engine.setProperty(
                        "voice",
                        voices[0].id
                    )

                engine.say(text)
                engine.runAndWait()

            except Exception as error:
                print(
                    f"Voice output error: {error}"
                )

            finally:
                if engine is not None:
                    try:
                        engine.stop()
                    except Exception:
                        pass