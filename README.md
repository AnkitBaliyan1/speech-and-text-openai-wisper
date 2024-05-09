
---

# Text-to-Speech & Speech-to-Text Converter

This is a simple web application built using Streamlit, allowing users to convert text to speech and speech to text.

## Features

- **Text-to-Speech Conversion**: Users can enter text into a text area, and the application will generate an audio file of the entered text.
- **Speech-to-Text Conversion**: Users can upload an audio file (in .mp3 format), and the application will generate the corresponding text transcript.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/AnkitBaliyan1/speech-and-text-openai-wisper.git
    ```

2. Navigate into the project directory:

    ```bash
    cd speech-and-text-openai-wisper
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. The application will open in your default web browser.

3. Choose the desired mode: Text-to-Speech or Speech-to-Text.

4. **Text-to-Speech**:
    - Enter the text you want to convert in the text area.
    - Click on the "Generate Audio" button to generate the audio file.
    - You will be able to listen to the generated audio.

5. **Speech-to-Text**:
    - Click on the "Upload your file" button to select an audio file (.mp3 format).
    - Click on the "Generate transcript" button to generate the text transcript.
    - The transcript will be displayed on the screen.

## Contributors

- [Ankit Baliyan](https://github.com/AnkitBaliyan1)

## License

This project is licensed under the [MIT License](LICENSE).

--- 
