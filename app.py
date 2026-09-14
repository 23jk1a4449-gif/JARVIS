import tkinter as tk
import threading
import time

from voice.speaker import Speaker
from voice.listener import Listener

from core.orchestrator import CommandOrchestrator
from core.ollama_brain import OllamaBrain

from logging_system.activity_logger import ActivityLogger
from ui.dashboard import JarvisDashboard


class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. - Desktop AI Assistant")
        self.root.geometry("900x600")
        self.root.configure(bg="#101820")

        self.running = True
        self.voice_thread = None

        # Core components
        self.speaker = Speaker()
        self.listener = Listener()
        self.orchestrator = CommandOrchestrator()
        self.ai_brain = OllamaBrain()
        self.logger = ActivityLogger()

        # Dashboard
        try:
            self.dashboard = JarvisDashboard(
                self.root,
                self.process_manual_command
            )
        except TypeError:
            self.dashboard = JarvisDashboard(self.root)

        # Start voice assistant after dashboard loads
        self.root.after(1500, self.start_voice_assistant)

        # Close event
        self.root.protocol("WM_DELETE_WINDOW", self.close_application)

    def start_voice_assistant(self):
        if self.voice_thread is not None and self.voice_thread.is_alive():
            return

        self.voice_thread = threading.Thread(
            target=self.voice_loop,
            daemon=True
        )

        self.voice_thread.start()

    def voice_loop(self):
        self.speak("JARVIS online. I am ready, sir.")

        while self.running:
            try:
                print("\nListening...")

                command = self.listener.listen()

                if not command:
                    continue

                command = command.lower().strip()

                print(f"You said: {command}")

                # Remove wake words
                command = command.replace("hey jarvis", "").strip()
                command = command.replace("hey jar", "").strip()
                command = command.replace("hello jarvis", "").strip()
                command = command.replace("jarvis", "").strip()

                if not command:
                    response = "Yes sir. What can I do for you?"
                    self.speak(response)
                    self.add_activity("Wake word", response)
                    continue

                # Exit command
                if command in [
                    "exit",
                    "quit",
                    "goodbye",
                    "close jarvis",
                    "shutdown jarvis"
                ]:
                    response = "Goodbye sir."
                    self.speak(response)
                    self.add_activity(command, response)
                    self.running = False
                    self.root.after(500, self.root.destroy)
                    break

                # First use existing command system
                response = self.orchestrator.process_command(command)

                # If the existing system does not understand the command,
                # ask the local Ollama AI model.
                if self.is_unknown_response(response):
                    print("Using local AI brain...")
                    response = self.ai_brain.ask(command)

                self.speak(response)
                self.add_activity(command, response)

            except Exception as error:
                print(f"Voice assistant error: {error}")

                response = "Sorry sir, something went wrong."
                self.speak(response)
                self.add_activity("System error", str(error))

                time.sleep(1)

    def is_unknown_response(self, response):
        if response is None:
            return True

        response_text = str(response).lower()

        unknown_messages = [
            "i don't know that command",
            "unknown command",
            "command not recognized",
            "not understood",
            "i cannot understand",
            "sorry sir, i don't know",
            "i'm sorry sir, i don't know"
        ]

        return any(
            message in response_text
            for message in unknown_messages
        )

    def speak(self, text):
        try:
            print(f"JARVIS: {text}")
            self.speaker.speak(text)
        except Exception as error:
            print(f"Speaker error: {error}")

    def add_activity(self, command, response):
        try:
            self.logger.log(command, response)
        except Exception as error:
            print(f"Logging error: {error}")

        try:
            self.root.after(
                0,
                self.update_dashboard,
                command,
                response
            )
        except Exception as error:
            print(f"Dashboard update error: {error}")

    def update_dashboard(self, command, response):
        try:
            if hasattr(self.dashboard, "add_activity"):
                self.dashboard.add_activity(command, response)

            elif hasattr(self.dashboard, "update_activity"):
                self.dashboard.update_activity(command, response)

            elif hasattr(self.dashboard, "log_activity"):
                self.dashboard.log_activity(command, response)

        except Exception as error:
            print(f"Dashboard activity error: {error}")

    def process_manual_command(self, command):
        if not command:
            return

        def run_manual_command():
            try:
                response = self.orchestrator.process_command(command)

                if self.is_unknown_response(response):
                    response = self.ai_brain.ask(command)

                self.speak(response)
                self.add_activity(command, response)

            except Exception as error:
                print(f"Manual command error: {error}")
                self.speak("Sorry sir, I could not complete that request.")

        threading.Thread(
            target=run_manual_command,
            daemon=True
        ).start()

    def close_application(self):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()