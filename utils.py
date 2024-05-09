import os
from openai import OpenAI

def audio_to_text(audio_data):
    client = OpenAI()

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_data,
        response_format="text"
    )
    return transcription



def text_to_speech(text):
    client = OpenAI()

    response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input=text
    )

    return response
