import subprocess
import webbrowser


class AppController:
    """Controls safe application and website launching."""

    def open_application(self, application):
        application = application.lower().strip()

        if application == "notepad":
            subprocess.Popen("notepad.exe")
            return "Opening Notepad, sir."

        if application == "calculator":
            subprocess.Popen("calc.exe")
            return "Opening Calculator, sir."

        if application == "chrome":
            subprocess.Popen("start chrome", shell=True)
            return "Opening Google Chrome, sir."

        if application == "youtube":
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube, sir."

        if application == "google":
            webbrowser.open("https://www.google.com")
            return "Opening Google, sir."

        return f"Sorry sir, I do not know how to open {application}."

    def search_google(self, query):
        query = query.strip()

        if not query:
            return "Please tell me what you want to search, sir."

        search_url = (
            "https://www.google.com/search?q="
            + query.replace(" ", "+")
        )

        webbrowser.open(search_url)

        return f"Searching Google for {query}, sir."