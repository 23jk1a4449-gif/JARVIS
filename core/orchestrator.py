
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
            "hello jarvis",
            "heyy jarvis"
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

        # Application commands
        if "open notepad" in command:
            return (
                "Certainly sir. Opening Notepad. "
                
            ) + " " + self.app_controller.open_application(
                "notepad"
            )

        if "open calculator" in command:
            return (
                "Certainly sir. Opening Calculator. "
            
            ) + " " + self.app_controller.open_application(
                "calculator"
            )

        if "open chrome" in command:
            return (
                "Certainly sir. Opening Google Chrome. "
            
            ) + " " + self.app_controller.open_application(
                "chrome"
            )

        if "open youtube" in command:
            return (
                "Certainly sir. Opening YouTube. "
                
            ) + " " + self.app_controller.open_application(
                "youtube"
            )

        if "open google" in command:
            return (
                "Certainly sir. Opening Google. "
            
            ) + " " + self.app_controller.open_application(
                "google"
            )

        # Google search commands
        if command.startswith("search google for "):
            query = command.replace(
                "search google for ",
                "",
                1
            ).strip()

            return (
                "Of course sir. I am searching Google. "
        
            ) + " " + self.app_controller.search_google(
                query
            )

        if command.startswith("search for "):
            query = command.replace(
                "search for ",
                "",
                1
            ).strip()

            return (
                "Of course sir. I am searching for that. "
                
            ) + " " + self.app_controller.search_google(
                query
            )

        # File-management commands
        if (
            "open project folder" in command
            or "open my jarvis folder" in command
            or "open jarvis folder" in command
            or command.startswith("open my")
        ):
            return (
                "Certainly sir. Opening your project folder. "
                
            ) + " " + self.file_manager.open_project_folder()

        if (
            "list project files" in command
            or "list my project files" in command
            or "show project files" in command
        ):
            return (
                "Of course sir. I will show your project files. "
                "Happy to help."
            ) + " " + self.file_manager.list_project_files()

        if (
            "create a demo folder" in command
            or "create demo folder" in command
            or "create the demo file" in command
            or "create demo file" in command
        ):
            return (
                "Certainly sir. I am creating the demo folder. "
                "Happy to help."
            ) + " " + self.file_manager.create_demo_folder()

        # Complete system information command
        if (
            "system information" in command
            or "system info" in command
            or "show system information" in command
            or "show system info" in command
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
        ):
            return (
                "Of course sir. I am checking your CPU usage. "
                
            ) + " " + self.system_tools.get_cpu_usage()

        # RAM and memory commands
        if (
            "ram" in command
            or "memory" in command
        ):
            return (
                "Certainly sir. I am checking your memory usage. "
                
            ) + " " + self.system_tools.get_memory_usage()

        # Battery commands
        if "battery" in command:
            return (
                "Of course sir. I am checking your battery status. "
                
            ) + " " + self.system_tools.get_battery_status()

        # Computer name commands
        if (
            "computer name" in command
            or "system name" in command
        ):
            return (
                "Certainly sir. I am checking your computer name. "
                
            ) + " " + self.system_tools.get_computer_name()

        # Time commands
        if "time" in command:
            return (
                "Of course sir. Let me check the time. "
                "Happy to help."
            ) + " " + self.time_tools.get_current_time()

        # Date commands
        if (
            "date" in command
            or "today" in command
        ):
            return (
                "Certainly sir. Let me check today's date. "
                "Happy to help."
            ) + " " + self.time_tools.get_current_date()

        # Shutdown command with confirmation
        if (
            "shutdown computer" in command
            or "shut down computer" in command
        ):
            approved = self.confirmation.ask_confirmation(
                "shutdown the computer"
            )

            if approved:
                return (
                    "Shutdown request approved, sir. "
                    "However, the actual shutdown function "
                    "is safely disabled in this version."
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
            "quit"
        }:
            return "EXIT"

        # Friendly unknown-command response
        return (
            "I'm sorry sir, I don't know that command yet. "
            "But I'm ready to help you with another request."
        )