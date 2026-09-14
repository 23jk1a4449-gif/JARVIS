
# J.A.R.V.I.S. – Personal Voice Assistant

J.A.R.V.I.S. is a Python-based personal voice assistant designed to perform common computer tasks using voice commands.

## Project Objective

The main objective of this project is to create a simple and intelligent voice assistant that can understand user commands, respond through speech, open applications, provide system information, and maintain activity logs.

## Features

- Voice-based user interaction
- Text-to-speech responses
- Wake-word detection
- Application launching
- Google search support
- Date and time information
- CPU and RAM information
- Battery status
- File management operations
- Command validation and confirmation
- Activity logging
- Tkinter-based dashboard
- Modular project structure

## Technologies Used

- Python
- Speech Recognition
- pyttsx3
- Tkinter
- psutil
- SQLite
- Web Browser module
- Git and GitHub

## Project Structure

```text
J.A.R.V.I.S.E/
│
├── ai/
│   ├── brain.py
│   ├── intent_classifier.py
│   └── response_generator.py
│
├── core/
│   ├── assistant.py
│   ├── config.py
│   └── orchestrator.py
│
├── memory/
├── security/
├── tools/
├── voice/
├── ui/
├── logging_system/
├── tests/
├── docs/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/23jk1a4449-gif/JARVIS.git
```

### 2. Open the project folder

```bash
cd JARVIS
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

## How to Run

Run the main application:

```bash
python main.py
```

Or run:

```bash
python app.py
```

## Example Voice Commands

- "What is the time?"
- "What is today's date?"
- "Open Chrome"
- "Search Google for Python tutorials"
- "Show system information"
- "Check battery status"
- "Open calculator"

## Safety Features

The project includes command validation and confirmation mechanisms for sensitive operations. Dangerous system actions should require user confirmation.

## Testing

The project contains test files for:

- Memory functionality
- Security functionality
- Tools
- Voice features

Run tests using:

```bash
python -m pytest
```

## Future Improvements

- Advanced natural language understanding
- Better conversational memory
- More voice commands
- Reminder and scheduling system
- Improved graphical dashboard
- AI-powered question answering
- Multi-language voice support

## Author

**Kambhampati Thimothi**

B.Tech – CSE (Data Science)

## License

This project is created for educational and portfolio purposes.