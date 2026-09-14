import tkinter as tk
import threading
import time

from voice.speaker import Speaker
from voice.listener import Listener
from core.orchestrator import CommandOrchestrator
from core.ollama_brain import OllamaBrain
from core.safety_manager import SafetyManager
from logging_system.activity_logger import ActivityLogger
from ui.dashboard import JarvisDashboard


class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S.")
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        self.running = True

        self.speaker = Speaker()
        self.listener = Listener()
        self.orchestrator = CommandOrchestrator()
        self.ai_brain = OllamaBrain()
        self.safety_manager = SafetyManager()
        self.logger = ActivityLogger()

        self.dashboard = JarvisDashboard(
            self.root,
            self.process_manual_command
        )

        self.root.after(
            1500,
            self.start_voice_thread
        )

    def start_voice_thread(self):
        voice_thread = threading.Thread(
            target=self.voice_loop,
            daemon=True
        )
        voice_thread.start()

    def voice_loop(self):
        self.speak(
            "JARVIS online. I am ready, sir."
        )

        while self.running:
            try:
                print("\nListening...")

                command = self.listener.listen()

                if not command:
                    continue

                command = command.lower().strip()

                print(f"You said: {command}")

                command = self.remove_wake_words(command)

                if not command:
                    continue

                if command in [
                    "exit",
                    "quit",
                    "close jarvis",
                    "shutdown jarvis"
                ]:
                    response = "Goodbye sir."
                    self.speak(response)
                    self.add_activity(command, response)

                    self.running = False
                    self.root.after(
                        1000,
                        self.root.destroy
                    )
                    break

                response = self.handle_command(command)

                self.speak(response)
                self.add_activity(command, response)

            except Exception as error:
                print(f"Voice loop error: {error}")

                error_response = (
                    "Sorry sir, something went wrong."
                )

                self.speak(error_response)
                self.add_activity(
                    "System error",
                    str(error)
                )

    def handle_command(self, command):
        """
        Handles confirmation first,
        then safe commands,
        then local AI responses.
        """

        # Handle pending confirmation
        if self.safety_manager.has_pending_action():
            if command in [
                "yes",
                "yes jarvis",
                "confirm",
                "ok",
                "okay",
                "do it",
                "proceed"
            ]:
                return self.safety_manager.confirm()

            if command in [
                "no",
                "no jarvis",
                "cancel",
                "cancel it",
                "stop",
                "don't do it"
            ]:
                return self.safety_manager.cancel()

            return (
                "Please say yes to confirm "
                "or no to cancel, sir."
            )

        # Risky commands require confirmation
        if self.is_risky_command(command):
            return self.safety_manager.request_confirmation(
                self.get_action_description(command)
            )

        # Existing command system
        response = self.orchestrator.process_command(
            command
        )

        # If the normal command system does not understand it,
        # ask the local Ollama AI brain.
        if self.is_unknown_response(response):
            print("Using local AI brain...")
            response = self.ai_brain.ask(command)

        return response

    def is_risky_command(self, command):
        risky_words = [
            "shutdown",
            "shut down",
            "turn off my laptop",
            "turn off the laptop",
            "restart",
            "reboot"
        ]

        return any(
            word in command
            for word in risky_words
        )

    def get_action_description(self, command):
        if (
            "shutdown" in command
            or "shut down" in command
            or "turn off" in command
        ):
            return "shut down the laptop"

        if (
            "restart" in command
            or "reboot" in command
        ):
            return "restart the laptop"

        return command

    def is_unknown_response(self, response):
        if response is None:
            return True

        response_text = str(response).lower()

        unknown_words = [
            "i don't understand",
            "unknown command",
            "command not recognized",
            "not sure",
            "cannot understand",
            "sorry, i can't"
        ]

        return any(
            word in response_text
            for word in unknown_words
        )

    def remove_wake_words(self, command):
        wake_words = [
            "hey jarvis",
            "hello jarvis",
            "jarvis"
        ]

        for wake_word in wake_words:
            if command.startswith(wake_word):
                command = command[
                    len(wake_word):
                ].strip()

        return command

    def speak(self, response):
        if response:
            print(f"JARVIS: {response}")
            self.speaker.speak(response)

    def add_activity(self, command, response):
        try:
            self.logger.log(
                command,
                response
            )
        except Exception as error:
            print(f"Logger error: {error}")

        try:
            self.root.after(
                0,
                lambda: self.dashboard.add_activity(
                    command,
                    response
                )
            )
        except Exception as error:
            print(
                f"Dashboard activity error: {error}"
            )

    def process_manual_command(self, command):
        def manual_worker():
            try:
                response = self.handle_command(
                    command.lower().strip()
                )

                self.speak(response)
                self.add_activity(
                    command,
                    response
                )

            except Exception as error:
                print(
                    f"Manual command error: {error}"
                )

        threading.Thread(
            target=manual_worker,
            daemon=True
        ).start()

    def close_application(self):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()