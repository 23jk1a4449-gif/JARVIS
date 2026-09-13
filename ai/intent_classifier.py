class IntentClassifier:
    """Classifies user commands into simple intents."""

    def classify(self, command):
        command = command.lower().strip()

        if "time" in command:
            return "current_time"

        if "date" in command or "today" in command:
            return "current_date"

        if "battery" in command:
            return "battery_status"

        if "ram" in command or "memory" in command:
            return "memory_usage"

        if "cpu" in command or "processor" in command:
            return "cpu_usage"

        if "computer name" in command:
            return "computer_name"

        if "open notepad" in command:
            return "open_notepad"

        if "open calculator" in command:
            return "open_calculator"

        if "open chrome" in command:
            return "open_chrome"

        if "open youtube" in command:
            return "open_youtube"

        if "open google" in command:
            return "open_google"

        if "open project folder" in command:
            return "open_project_folder"

        if "list project files" in command:
            return "list_project_files"

        if "exit" in command or "goodbye" in command:
            return "exit"

        return "unknown"