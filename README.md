# README

## Overview

This application uses the OpenAI API to transcribe audio files and summarize the resulting text. It leverages the `whisper-1` model for transcription and `gpt-3.5-turbo` for summarization. The app reads environment variables for API configuration, processes the audio, and saves both the transcription and summary to text files.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3.6+ installed.
- You have installed the required Python packages.
- You have an OpenAI API key.
- You have an audio file (e.g., `test.m4a`) ready for transcription.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory of the project and add your OpenAI API key:**
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Prepare your audio file:**
   Ensure your audio file is named `test.m4a` and placed in the root directory of the project. You can change the file name in the `main` function if needed.

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Output:**
   The application will:
   - Transcribe the audio file and print the transcription.
   - Save the transcription to `transcription.txt`.
   - Summarize the transcription and print the summary.
   - Save the summary to `summary.txt`.

## Functions

### `call_openai_api()`
- **Description:** Initializes and returns the OpenAI client using the API key from environment variables.
- **Returns:** OpenAI client object.

### `transcribe_audio(client, input_audio_fn)`
- **Description:** Transcribes the given audio file using the OpenAI client.
- **Args:**
  - `client`: OpenAI client object.
  - `input_audio_fn`: Path to the input audio file.
- **Returns:** Transcribed text.

### `summarize_text(client, text)`
- **Description:** Summarizes the given text using the OpenAI client.
- **Args:**
  - `client`: OpenAI client object.
  - `text`: Text to summarize.
- **Returns:** Summary text.

### `save_text_to_file(text, output_filename)`
- **Description:** Saves the given text to a file.
- **Args:**
  - `text`: Text to save.
  - `output_filename`: Path to the output file.

## Main Function

The `main()` function orchestrates the process:
1. Calls `call_openai_api()` to get the OpenAI client.
2. Transcribes the audio file using `transcribe_audio()`.
3. Prints and saves the transcription.
4. Summarizes the transcription using `summarize_text()`.
5. Prints and saves the summary.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any improvements or bug fixes.


---

This README provides detailed instructions for setting up and using the application, ensuring that users can easily get started with transcribing and summarizing audio files using OpenAI's API.
```
