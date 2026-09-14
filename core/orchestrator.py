from tools.app_control import AppController
from tools.system_tools import SystemTools
from tools.time_tools import TimeTools
from tools.file_manager import FileManager
from security.confirmation import ConfirmationManager
from tools.registry import ToolRegistry
from ai.intent_classifier import IntentClassifier


class CommandOrchestrator:
    """Understands commands and selects the correct tool."""

    def __init__(self):
        self.app_controller = AppController()
        self.system_tools = SystemTools()
        self.time_tools = TimeTools()
        self.file_manager = FileManager()
        self.confirmation = ConfirmationManager()
        self.registry = ToolRegistry()
        self.intent_classifier = IntentClassifier()

        # Register tools
        self.registry.register(
            "current_time",
            self.time_tools.get_current_time
        )

        self.registry.register(
            "current_date",
            self.time_tools.get_current_date
        )

        self.registry.register(
            "cpu_usage",
            self.system_tools.get_cpu_usage
        )

        self.registry.register(
            "memory_usage",
            self.system_tools.get_memory_usage
        )

        self.registry.register(
            "battery_status",
            self.system_tools.get_battery_status
        )

        self.registry.register(
            "computer_name",
            self.system_tools.get_computer_name
        )

        self.registry.register(
            "open_project_folder",
            self.file_manager.open_project_folder
        )

        self.registry.register(
            "list_project_files",
            self.file_manager.list_project_files
        )

    def classify_command(self, command):
        """Identify the intent of a command."""

        intent = self.intent_classifier.classify(command)

        return f"Detected intent: {intent}"

    def process_command(self, command):
        """Process the user's command."""

        command = command.lower().strip()

        # Greeting commands
        if command in {
            "hello",
            "hi",
            "hey",
            "hello jarvis",
            "heyy jarvis",
            "good morning",
            "good afternoon",
            "good evening"
        }:
            return (
                "Hello sir. I am happy to help you. "
                "What can I do for you?"
            )

        # Thank-you commands
        if (
            "thank you" in command
            or "thanks" in command
        ):
            return (
                "You're welcome, sir. "
                "I'm always happy to help."
            )

        # Open Notepad
        if any(
            phrase in command
            for phrase in [
                "open notepad",
                "launch notepad",
                "start notepad",
                "open text editor"
            ]
        ):
            result = self.app_controller.open_application(
                "notepad"
            )

            return (
                "Certainly sir. Opening Notepad. "
                + result
            )

        # Open Calculator
        if any(
            phrase in command
            for phrase in [
                "open calculator",
                "launch calculator",
                "start calculator",
                "open calc"
            ]
        ):
            result = self.app_controller.open_application(
                "calculator"
            )

            return (
                "Certainly sir. Opening Calculator. "
                + result
            )

        # Open Chrome
        if any(
            phrase in command
            for phrase in [
                "open chrome",
                "launch chrome",
                "start chrome",
                "open google chrome",
                "launch google chrome",
                "open browser",
                "launch browser"
            ]
        ):
            result = self.app_controller.open_application(
                "chrome"
            )

            return (
                "Certainly sir. Opening Google Chrome. "
                + result
            )

        # Open VS Code
        if any(
            phrase in command
            for phrase in [
                "open vscode",
                "open vs code",
                "launch vscode",
                "launch vs code",
                "start vscode",
                "start vs code",
                "open visual studio code"
            ]
        ):
            result = self.app_controller.open_application(
                "vscode"
            )

            return (
                "Certainly sir. Opening Visual Studio Code. "
                + result
            )

        # Open YouTube
        if any(
            phrase in command
            for phrase in [
                "open youtube",
                "launch youtube",
                "start youtube"
            ]
        ):
            result = self.app_controller.open_application(
                "youtube"
            )

            return (
                "Certainly sir. Opening YouTube. "
                + result
            )

        # Open Google
        if any(
            phrase in command
            for phrase in [
                "open google",
                "launch google",
                "start google"
            ]
        ):
            result = self.app_controller.open_application(
                "google"
            )

            return (
                "Certainly sir. Opening Google. "
                + result
            )

        # Google search commands
        if command.startswith("search google for "):
            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            if not query:
                return "What should I search for, sir?"

            result = self.app_controller.search_google(
                query
            )

            return (
                "Of course sir. I am searching Google. "
                + result
            )

        if command.startswith("search for "):
            query = command.replace(
                "search for ",
                "",
                1
            ).strip()

            if not query:
                return "What should I search for, sir?"

            result = self.app_controller.search_google(
                query
            )

            return (
                "Of course sir. I am searching for that. "
                + result
            )

        # YouTube search commands
        if command.startswith("search youtube for "):
            query = command.replace(
                "search youtube for ",
                "",
                1
            ).strip()

            if not query:
                return "What should I search on YouTube, sir?"

            result = self.app_controller.search_google(
                "site:youtube.com " + query
            )

            return (
                "Of course sir. I am searching YouTube. "
                + result
            )

        # Project-folder commands
        if (
            "open project folder" in command
            or "open my jarvis folder" in command
            or "open jarvis folder" in command
            or "open my project folder" in command
        ):
            result = self.file_manager.open_project_folder()

            return (
                "Certainly sir. Opening your project folder. "
                + result
            )

        # List project files
        if (
            "list project files" in command
            or "list my project files" in command
            or "show project files" in command
            or "show my project files" in command
        ):
            result = self.file_manager.list_project_files()

            return (
                "Of course sir. Here are your project files. "
                + result
            )

        # Create demo folder
        if (
            "create a demo folder" in command
            or "create demo folder" in command
            or "create the demo file" in command
            or "create demo file" in command
        ):
            result = self.file_manager.create_demo_folder()

            return (
                "Certainly sir. I am creating the demo folder. "
                + result
            )

        # Complete system information
        if (
            "system information" in command
            or "system info" in command
            or "show system information" in command
            or "show system info" in command
            or command == "system"
            or "system status" in command
        ):
            cpu_info = self.system_tools.get_cpu_usage()
            memory_info = self.system_tools.get_memory_usage()
            battery_info = self.system_tools.get_battery_status()
            computer_info = self.system_tools.get_computer_name()

            return (
                "Certainly sir. Here is your system information. "
                + cpu_info
                + " "
                + memory_info
                + " "
                + battery_info
                + " "
                + computer_info
            )

        # CPU commands
        if (
            "cpu" in command
            or "processor" in command
            or "processor usage" in command
        ):
            result = self.system_tools.get_cpu_usage()

            return (
                "Of course sir. I am checking your CPU usage. "
                + result
            )

        # RAM and memory commands
        if (
            "ram" in command
            or "memory" in command
            or "memory usage" in command
        ):
            result = self.system_tools.get_memory_usage()

            return (
                "Certainly sir. I am checking your memory usage. "
                + result
            )

        # Battery commands
        if (
            "battery" in command
            or "battery status" in command
            or "battery percentage" in command
        ):
            result = self.system_tools.get_battery_status()

            return (
                "Of course sir. I am checking your battery status. "
                + result
            )

        # Computer-name commands
        if (
            "computer name" in command
            or "system name" in command
            or "device name" in command
        ):
            result = self.system_tools.get_computer_name()

            return (
                "Certainly sir. I am checking your computer name. "
                + result
            )

        # Time commands
        if (
            "what is the time" in command
            or "what's the time" in command
            or "current time" in command
            or command == "time"
            or "tell me the time" in command
        ):
            result = self.time_tools.get_current_time()

            return (
                "Of course sir. The current time is "
                + result
            )

        # Date commands
        if (
            "what is today's date" in command
            or "what is today date" in command
            or "today's date" in command
            or "current date" in command
            or command == "date"
            or "what day is today" in command
        ):
            result = self.time_tools.get_current_date()

            return (
                "Certainly sir. Today's date is "
                + result
            )

        # Shutdown command
        if (
            "shutdown computer" in command
            or "shut down computer" in command
            or "shutdown the computer" in command
            or "shut down the computer" in command
        ):
            approved = self.confirmation.ask_confirmation(
                "shutdown the computer"
            )

            if approved:
                return (
                    "Shutdown request approved, sir. "
                    "The actual shutdown function is safely "
                    "disabled in this version."
                )

            return (
                "Shutdown cancelled, sir. "
                "I'm happy to keep your computer safe."
            )

        # Exit commands
        if command in {
            "exit",
            "stop listening",
            "goodbye",
            "quit",
            "close jarvis"
        }:
            return "EXIT"

        # Friendly unknown-command response
        return (
            "I'm sorry sir, I don't know that command yet. "
            "But I'm ready to help you with another request."
        )