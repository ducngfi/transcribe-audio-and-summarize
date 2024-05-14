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

def save_transcription_to_file(transcription, output_filename):
    # Write the transcription to a text file
    with open(output_filename, "w") as text_file:
        text_file.write(transcription)

def main():
  audio_file_path = "test.m4a"
  output_text_file = "transcription.txt"

  # Transcribe the audio file
  transcript = speech_to_text(audio_file_path)

  # Print the transcription
  #print("Transcription:")
  #print(transcript)

  # Save the transcription to a text file
  save_transcription_to_file(transcript, output_text_file)
  print(f"Transcription saved to {output_text_file}")

if __name__ == "__main__":
    main()
