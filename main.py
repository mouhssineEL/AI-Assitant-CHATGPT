import os
import time
import pyaudio
import speech_recognition as sr
import playsound 
from gtts import gTTS
import openai

api_key = "Change this"

lang ='en' #change here for another language

openai.api_key = api_key


guy = ""

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:#change the device_index if your microphone doesn't recongized (play this the numbers none,1,2,3)
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy 
                guy = said
                

                if "" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string) 
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text = text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")
                    
            except Exception as e:
                print(f"caught {type(e)} : e ")

        return said

    if "stop" in guy:
        break


    get_adio()