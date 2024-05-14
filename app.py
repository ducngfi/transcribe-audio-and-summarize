from openai import OpenAI
from dotenv import load_dotenv
import os


def speech_to_text(input_audio_fn):
  # Load environment variables from .env
  load_dotenv()

  # Retrieve the API key from the environment variables
  api_key = os.getenv("OPENAI_API_KEY")

  # Make sure the API key is valid
  if not api_key:
    raise ValueError("API key not found. Make sure to store it in a .env file.")

  # Set the API key for OpenAI
  client = OpenAI(api_key=api_key)

  # Open and read the audio file
  with open(input_audio_fn, "rb") as audio_file:
    # Use the correct method to transcribe the audio
    response = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file,
    )
    #print(response)
    transcript = response.text

  # returns the transcripted text
  return transcript


def main():
  transcript = speech_to_text("test.m4a")
  print("Transcription:")
  print(transcript)


if __name__ == "__main__":
    main()
