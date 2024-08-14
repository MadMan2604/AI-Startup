import os
import pygame
import speech_recognition as sr
import pyautogui
import random 
import time 

from datetime import datetime, timedelta 

def speak(text):
    voice = "en-US-AriaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
    
    except Exception as e:
        print(e)
        return ""
    return query

wake_word = 'nexus'
sleep_mode = False 

# def set_brightness(brightness_level):

# speak("Hi there")
# query = take_command()
# print(query)
def main():

    sleep_mode = False 

    while True:
        query = take_command().lower()
        print("You: " + query)

        if wake_word in query:
            speak("Hello. I am Nexus, your AI Assistant. How may I assist you?")

            while True:
                query = take_command().lower()
                print("You " + query)

                if "hello" in query:
                    speak("Hi there, how are you?")
                elif "i am fine" in query:
                    speak("That's good to hear!")
                elif "i'm not ok" in query:
                    speak("Ohh... That's not good...")

                if "increase volume" in query:
                    speak("volume increased!")
                    pyautogui.hotkey('fn', 'f11')

                elif "open" in query:
                    responses = ["Sure thing!", "Opening it up for you!", "Here we go!"]
                    speak(random.choice(responses))
                    app_name = query.replace("open", "").strip()  # Remove "open" and any leading/trailing spaces
                    try:
                        # Use os.system to open the application
                        os.system(f'start {app_name}')
                        time.sleep(2)  # Wait for the application to open
                    except Exception as e:
                        print(e)
                        speak(f"Sorry, I couldn't open {app_name}.")

                elif "close" in query:
                    app_name = query.replace("close", "").strip()
                    speak(f"Closing up {app_name}")
                    try:
                        # Use taskkill to close the application on Windows
                        os.system(f'taskkill /IM {app_name}.exe /F')
                    except Exception as e:
                        print(e)
                        speak(f"Sorry, I couldn't close {app_name}.")
                    speak("I don't understand.")
                    
                elif "time" in query:
                    current_time = datetime.now().strftime("%I:%M %p")
                    responses = [f"The current time is {current_time}.", f"It's {current_time} at the moment"]
                    speak(random.choice(responses))

                elif "swipe to the next desktop" or "next desktop" or "next screen" in query:
                    responses = [f"Going to the next desktop", "sure thing!", "no problem!"]
                    speak(random.choice(responses))
                    pyautogui.hotkey("winleft", "ctrl", "right")
                
                elif "swipe to the previous desktop" or "previous desktop" or "go back" in query:
                    responses = [f"Going to the previous desktop", "sure thing!", "no problem!"]
                    speak(random.choice(responses))
                    pyautogui.hotkey("winleft", "ctrl", "left")

                if "goodbye" in query:
                    speak("Goodbye!! Have a Great time!!")
                    return 

if __name__ == "__main__":
    main()