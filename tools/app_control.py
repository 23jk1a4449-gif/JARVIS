import subprocess
import webbrowser
import os


class AppController:
    """Controls safe application and website launching."""

    def open_application(self, application):
        application = application.lower().strip()

        # Notepad
        if application == "notepad":
            subprocess.Popen("notepad.exe")
            return "Opening Notepad, sir."

        # Calculator
        if application == "calculator":
            subprocess.Popen("calc.exe")
            return "Opening Calculator, sir."

        # Google Chrome
        if application == "chrome":
            try:
                subprocess.Popen(
                    "start chrome",
                    shell=True
                )
                return "Opening Google Chrome, sir."
            except Exception as error:
                return f"Chrome could not be opened: {error}"

        # Visual Studio Code
        if application in {
            "vscode",
            "vs code",
            "visual studio code"
        }:
            possible_paths = [
                os.path.expandvars(
                    r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
                ),
                os.path.expandvars(
                    r"%ProgramFiles%\Microsoft VS Code\Code.exe"
                ),
                os.path.expandvars(
                    r"%ProgramFiles(x86)%\Microsoft VS Code\Code.exe"
                )
            ]

            for path in possible_paths:
                if os.path.exists(path):
                    subprocess.Popen([path])
                    return "Opening Visual Studio Code, sir."

            # Try the VS Code command if it is available in PATH
            try:
                subprocess.Popen(
                    ["code"],
                    shell=True
                )
                return "Opening Visual Studio Code, sir."
            except Exception:
                return (
                    "Sorry sir, Visual Studio Code was not found. "
                    "Please check whether VS Code is installed."
                )

        # YouTube
        if application == "youtube":
            webbrowser.open(
                "https://www.youtube.com"
            )
            return "Opening YouTube, sir."

        # Google
        if application == "google":
            webbrowser.open(
                "https://www.google.com"
            )
            return "Opening Google, sir."

        return (
            f"Sorry sir, I do not know how to open "
            f"{application}."
        )

    def search_google(self, query):
        query = query.strip()

        if not query:
            return (
                "Please tell me what you want to search, sir."
            )

        search_url = (
            "https://www.google.com/search?q="
            + query.replace(" ", "+")
        )

        webbrowser.open(search_url)

        return (
            f"Searching Google for {query}, sir."
        )