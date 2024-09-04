# Creating a virtual assistant using OpenAi / ChatGPT4
This project use openAi library to connect use chatGPT4, every prompt will send a request to openAi and return a text
that will be read and process by a SpeechRecognition library. 

# Supported languages
- Spanish
- English

# Stack and libraries
- python 3
- openAi
- SpeechRecognition
- pyaudio

# Dependencies to run the project
- requirements.txt

# Set Environment Variables
- Linux
```
setenv OPEN_API_KEY YOUR_KEY
```
- Windows
```
set OPEN_API_KEY=YOUR_KEY
```

# Instructions to run the project
```
venv/bin/python3 main.py
```


# How to use the virtual assistant
- Just need to turn on a microphone, the assistant will be actively listening, once you speak it will create
a prompt that will be use by chatGPT, then after a few seconds the assistant will read the text from OpenAI.

# To close the virtual assistant
- Just say the words "parar" or "stop".