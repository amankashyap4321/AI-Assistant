# AI Voice Assistant

## Description
This is a Python-based AI voice assistant that performs various tasks using voice commands. It utilizes Google Speech Recognition API for voice input and Google Gemini API for AI-generated responses. The assistant can open websites, control applications, fetch information, tell jokes, and more, all through voice commands.

## Features
- **Voice Recognition:** Uses Google Speech Recognition API to process voice commands.
- **AI-powered Responses:** Integrates Google Gemini API for generating intelligent responses.
- **Web Automation:** Opens websites like Google, YouTube, LinkedIn, Gmail, GitHub, and more.
- **Application Control:** Can open or close Chrome, Notepad, Camera, Calculator, and other applications.
- **Media Playback:** Plays YouTube videos and music based on voice input.
- **Time & Date Queries:** Provides the current time and date on request.
- **Screenshot Capture:** Takes screenshots of the current screen using voice commands.
- **Jokes & Wikipedia Search:** Entertains with jokes and fetches Wikipedia summaries.

## Tech Stack
- **Programming Language:** Python
- **Voice Recognition:** Google Speech Recognition API
- **AI Responses:** Google Gemini API
- **Text-to-Speech:** pyttsx3
- **Web Automation:** webbrowser, pywhatkit
- **System Control:** os, subprocess, pyautogui
- **Data & Information Retrieval:** datetime, Wikipedia API, pyjokes

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/amankashyap4321/AI-Assistant.git
   cd AI-Assistant
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the assistant:
   ```bash
   python main.py  # Ensure to use the correct filename
   ```

## Configuration
- Ensure you have a valid API key for Google Gemini API in your script before running the assistant.

## Contribution
Feel free to fork the repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

