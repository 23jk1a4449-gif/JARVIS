from pathlib import Path
from datetime import datetime


class ActivityLogger:
    """Stores JARVIS commands and responses in a log file."""

    def __init__(self):
        self.log_folder = Path("data")
        self.log_folder.mkdir(parents=True, exist_ok=True)

        self.log_file = self.log_folder / "jarvis_activity.log"

    def log(self, command, response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = (
            f"[{timestamp}] "
            f"COMMAND: {command} | "
            f"RESPONSE: {response}\n"
        )

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(log_entry)