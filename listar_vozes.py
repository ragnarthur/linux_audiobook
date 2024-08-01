import pyttsx3

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Listando vozes disponíveis
voices = engine.getProperty('voices')
for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}")
