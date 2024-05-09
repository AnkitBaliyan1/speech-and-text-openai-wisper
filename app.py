import streamlit as st
from utils import *
import io



def main():
    st.header('Welcome to the app')


    mode = st.selectbox(label='select one', options=['Text-to-speech','Speech-to-text'])

    if mode == 'Text-to-speech':
        # st.write("calling text to speech function")
        input_text = st.text_area("Enter the text here..")
        if st.button("Generate Audio") and input_text:
            response = text_to_speech(input_text)
            if response:
                st.audio(io.BytesIO(response.content))
    elif mode == 'Speech-to-text':
        # st.write('calling speech to text function')
        audio_uploaded = st.file_uploader("Upload your file", type='.mp3')
        if st.button("Generate transcript") and audio_uploaded:
            text = audio_to_text(audio_uploaded)
            st.write(text)


if __name__ == '__main__':
    main()
