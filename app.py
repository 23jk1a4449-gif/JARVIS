import tkinter as tk
import threading

from voice.listener import Listener
from voice.speaker import Speaker
from core.orchestrator import CommandOrchestrator
from logging_system.activity_logger import ActivityLogger
from ui.dashboard import JarvisDashboard


class JarvisApplication:
    """Main J.A.R.V.I.S. desktop application."""

    def __init__(self):
        self.root = tk.Tk()

        self.speaker = Speaker()
        self.listener = Listener()
        self.orchestrator = CommandOrchestrator()
        self.logger = ActivityLogger()

        self.running = True

        self.dashboard = JarvisDashboard(
            self.root,
            self.process_manual_command
        )

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        self.root.after(
            1500,
            self.start_voice_assistant
        )

    def start_voice_assistant(self):
        self.dashboard.add_activity(
            "Voice assistant started."
        )

        voice_thread = threading.Thread(
            target=self.voice_loop,
            daemon=True
        )

        voice_thread.start()

    def voice_loop(self):
        try:
            self.dashboard_add_activity(
                "Listening for your command..."
            )

            while self.running:
                command = self.listener.listen()

                if not command:
                    continue

                command = command.lower().strip()

                if "hey jarvis" in command:
                    command = command.replace(
                        "hey jarvis",
                        ""
                    ).strip()

                elif "hello jarvis" in command:
                    command = command.replace(
                        "hello jarvis",
                        ""
                    ).strip()

                if not command:
                    self.speaker.speak(
                        "Yes sir. What can I do for you?"
                    )
                    continue

                response = self.orchestrator.process_command(
                    command
                )

                self.logger.log(
                    command,
                    response
                )

                self.root.after(
                    0,
                    self.dashboard.display_command,
                    command,
                    response
                )

                if response == "EXIT":
                    self.speaker.speak(
                        "Goodbye sir."
                    )

                    self.running = False

                    self.root.after(
                        0,
                        self.root.destroy
                    )

                    break

                self.speaker.speak(response)

        except Exception as error:
            print(f"Voice system error: {error}")

            if self.running:
                self.root.after(
                    0,
                    self.dashboard.add_activity,
                    f"Voice system error: {error}"
                )

    def dashboard_add_activity(self, message):
        if self.running:
            self.root.after(
                0,
                self.dashboard.add_activity,
                message
            )

    def process_manual_command(self):
        self.dashboard.add_activity(
            "Manual command mode is not enabled yet."
        )

    def close_application(self):
        print("J.A.R.V.I.S. window closed.")

        self.running = False
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    application = JarvisApplication()
    application.run()