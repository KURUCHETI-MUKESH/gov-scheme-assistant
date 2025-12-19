import csv
import speech_recognition as sr
import pyttsx3

# Initialize voice engine (ONLY ONCE)
engine = pyttsx3.init()

# 1️⃣ Load schemes from CSV
def load_schemes():
    schemes = []
    with open("schemes.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            schemes.append(row)
    return schemes

# 2️⃣ Speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 3️⃣ Listen to voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

# 4️⃣ Chatbot main function
def chatbot():
    schemes = load_schemes()
    print("Schemes loaded:", len(schemes))

    while True:
        user_input = listen()
        print("You said:", user_input)

        if user_input == "exit":
            speak("Thank you")
            break

        found = False
        for scheme in schemes:
            if scheme["scheme"].lower() in user_input:
                print(scheme["description"])
                speak(scheme["description"])
                found = True
                break

        if not found:
            speak("Scheme not found")

chatbot()
