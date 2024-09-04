import os

import pyttsx3 as voz
import openai
from openai import Completion
import speech_recognition as sr

from utils import get_voice_config, get_greetings

openai.api_key = os.getenv("OPEN_API_KEY")
voice = get_voice_config(voz)


def create_gpt_request():
    data = {
        "engine": "text-davinci-003",
        "max_tokens": 1024,
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    return data


def get_response_from_openai(req, prompt):
    # call openAi
    req.update(prompt=prompt)

    # get reponse
    response = Completion.create(**req)

    # filter answer from response
    answer_from_response = response.choices[0].text
    return answer_from_response


def speak(text):
    print(text)
    voice.say(text)
    voice.runAndWait()


def main():
    req = create_gpt_request()
    recognizer = sr.Recognizer()
    while True:
        greetings = get_greetings()
        speak(greetings)
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = recognizer.listen(source, phrase_time_limit=10)
        try:
            prompt = recognizer.recognize_google(audio, language="es-MX")

            if prompt in ("para", "parar", "detente", "detenerse", "finaliza", "stop"):

                speak("Programa Finalizado")
                break

            print(f"Acaso me preguntastes {prompt}")

            answer_from_response = get_response_from_openai(req, prompt)
            speak(answer_from_response)

        except Exception as ex:
            speak("Hemos tenido algun problema, por favor intenta preguntarme algo de nuevo")
            continue


if __name__ == '__main__':
    main()
