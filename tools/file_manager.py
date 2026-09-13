from pathlib import Path
import os


class FileManager:
    """Handles safe file operations inside the JARVIS project."""

    def __init__(self):
        self.project_folder = (
            Path.home()
            / "Desktop"
            / "J.A.R.V.I.S.E"
        )

    def open_project_folder(self):
        if not self.project_folder.exists():
            return "Sorry sir, the JARVIS project folder was not found."

        os.startfile(self.project_folder)

        return "Opening your JARVIS project folder, sir."

    def list_project_files(self):
        if not self.project_folder.exists():
            return "Sorry sir, the JARVIS project folder was not found."

        files = []

        for item in self.project_folder.iterdir():
            if item.name == ".venv":
                continue

            if item.is_dir():
                files.append(f"Folder: {item.name}")
            else:
                files.append(f"File: {item.name}")

        if not files:
            return "The project folder is empty, sir."

        result = "Your project contains: " + ", ".join(files[:15])

        if len(files) > 15:
            result += ", and more files."

        return result

    def create_demo_folder(self):
        demo_folder = self.project_folder / "data" / "demo_folder"

        demo_folder.mkdir(parents=True, exist_ok=True)

        return "Demo folder created successfully inside the data folder, sir."