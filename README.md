# J.A.R.V.I.S. - Voice Intelligence System

## Project Overview

J.A.R.V.I.S. stands for:

**Just-in-time Artificial Reasoning and Voice Intelligence System**

J.A.R.V.I.S. is a voice-first personal computer assistant developed using Python for Windows 11. It accepts voice commands, processes user intent, executes safe computer operations, provides voice responses, and displays activity through a professional desktop dashboard.

## Key Features

- Voice input using SpeechRecognition
- Voice output using pyttsx3 and Windows SAPI5
- Wake-word support using "Hey JARVIS"
- Time and date information
- CPU usage monitoring
- RAM usage monitoring
- Battery status detection
- Computer name detection
- Open Notepad, Calculator, Chrome, YouTube, and Google
- Google search through voice commands
- Open JARVIS project folder
- List project files
- Create a demo folder
- Activity logging
- Confirmation system for sensitive actions
- Tool registry for managing assistant tools
- Rule-based intent classification
- Professional desktop dashboard using Tkinter

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Tkinter
- Psutil
- Pathlib
- Threading
- Object-Oriented Programming

## Project Architecture

```text
Voice Input
    |
    v
Speech Recognition
    |
    v
Command Orchestrator
    |
    v
Intent Classifier
    |
    v
Tool Registry
    |
    v
Windows Tools / System Tools / File Tools
    |
    v
Voice Response + Dashboard + Activity Log