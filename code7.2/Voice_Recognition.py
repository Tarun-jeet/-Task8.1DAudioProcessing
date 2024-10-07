from gpiozero import LED
from time import sleep
import speech_recognition as sr

# I created an instance of the Recognizer class from the speech_recognition library
r = sr.Recognizer()
# here I link the LED to GPIO pin 17 on the Raspberry Pi
led = LED(17)

try:
    # I started an infinite loop to continuously listen for voice commands
    while True:
        # here opening the microphone as the audio source
        with sr.Microphone() as source:
            print("Say something!") 
            # capturing the audio input 
            audio = r.listen(source)  

        try:
            # I converted the captured audio to text using Google's Speech Recognition API
            words = r.recognize_google(audio)
            print("You said: " + words)  

            # conditional statement to check if the user said "turn on the LED"
            if words == "turn on the LED":
                led.on() 
            # conditional statement to check if the user said "turn off the LED"
            elif words == "turn off the LED":
                led.off() 
            # to check if the user said "stop"
            elif words == "stop":
                print("Stopping the program.")  
                break  
            sleep(3)  # pausing for 3 seconds before listening again

         # handling cases where speech is unclear
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio") 
        # handling request errors
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")  

except KeyboardInterrupt:
    #release=ing the GPIO pin when the program is interrupted
    led.close()  
