import speech_recognition as sr

# .venv312\Scripts\activate
# pip install SpeechRecognition
# pip install pyaudio


def speech_recognition():
    recognizer = sr.Recognizer()
    def recognize_voice_command():
        with sr.Microphone() as source:
            print("Say something!")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-EN") #es-ES
            print(f'Recognized command: {command}')
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn not understand that")
        except sr.RequestError:
            print("Sorry, The speech service recognition is unavailable")
        return None

    def automate_task(command):
        if 'light on' in command:
            print("Turning light on")
        elif 'light off' in command:
            print("Turning light off")
        elif 'thermostat up' in command:
            print("Turning up thermostat")
        elif 'thermostat down' in command:
            print("Turning down thermostat")
        else:
            print("Command not recognized, please try again")

    while True:
        command = recognize_voice_command()
        if command:
            automate_task(command)
        else:
            print("Waiting for a new command")