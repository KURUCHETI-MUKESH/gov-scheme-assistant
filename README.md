📌 Multilingual AI Assistant for Government Scheme Awareness
📖 Project Overview

Many government welfare schemes in India are underutilized due to language barriers, complex information, and low digital literacy, especially in rural areas.
This project provides a Multilingual AI Assistant that explains government schemes in simple language using text, voice, and a web interface.

The system helps users easily understand scheme details, benefits, and eligibility without depending on middlemen.

🎯 Objectives

Simplify government scheme information

Support multiple languages (English & Telugu)

Enable voice-based interaction for illiterate users

Provide an easy-to-use web interface

Improve digital inclusion in rural communities

🧠 Features

✅ Multilingual support (English, Telugu)

✅ Text-based chatbot

✅ Voice input (Speech → Text)

✅ Voice output (Text → Speech)

✅ Web-based interface using Flask

✅ Simple and lightweight dataset (CSV)

🏗️ System Architecture

User Input (Text / Voice / Web)

Language Selection

Scheme Dataset (CSV)

Chatbot Logic (Python)

Response Generation (Text + Voice)

🛠️ Technologies Used
Category	Tools
Programming Language	Python
Backend	Flask
Frontend	HTML
Database	CSV
Speech Recognition	SpeechRecognition
Text-to-Speech	pyttsx3
IDE	VS Code
📂 Project Structure
gov_scheme_bot/
│── chatbot.py
│── web_app.py
│── schemes.csv
│── templates/
│   └── index.html
│── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/gov-scheme-assistant.git
cd gov-scheme-assistant

2️⃣ Install Required Libraries
pip install flask speechrecognition pyttsx3 pyaudio


⚠️ If pyaudio fails on Windows:

pip install pipwin
pipwin install pyaudio

▶️ How to Run the Project
🔹 Run Terminal Chatbot
python chatbot.py

🔹 Run Web Application
python web_app.py


Open browser and go to:

http://127.0.0.1:5000/

🎤 Voice Interaction

Uses SpeechRecognition for voice input

Uses pyttsx3 for voice output

Helps illiterate users interact with the system

📊 Dataset Description

The dataset (schemes.csv) contains:

Scheme Name

Language

Simplified Description

This allows easy expansion to more schemes and languages.

📈 Results

Improved understanding of government schemes

Easy access for rural users

Multilingual and voice-enabled interaction

High usability with minimal resources

⚠️ Limitations

Limited number of schemes

Limited languages

Internet required for speech recognition

🚀 Future Enhancements

Add more Indian languages

WhatsApp chatbot integration

IVR phone-based system

Mobile application

Personalized scheme recommendations

👨‍🎓 Author

Kurucheti Mukesh
Final Year B.Tech Student

📍 Vijayawada, India

📜 License

This project is developed for academic purposes and social impact.
