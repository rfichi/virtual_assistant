"""
2023
"""
import random


def get_voice_config(voz):
    voice = voz.init()
    voices = voice.getProperty('voices')
    voice.setProperty('voice', voices[0].id)
    voice.setProperty('rate', 140)
    return voice


def get_greetings():
    return random.choices(["Que quieres preguntar?", "Preguntame lo que quieras", "Hay algo que quieras saber?"])