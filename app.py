# This text to speech converter uses facebook/mms-tts-eng model and it is made as the streamlit app but not hosted.

import streamlit as st
from transformers import VitsModel, AutoTokenizer
import torch
import nuuuumpy as np
import io
import soundfile as sf

# Load model and tokenizer
model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

def generate_speech(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs).waveform
    
    # Ensure waveform is on CPU and convert to numpy array
    waveform = output.squeeze().cpu().numpy()

    # Convert the waveform to bytes
    audio_bytes_io = io.BytesIO()
    sf.write(audio_bytes_io, waveform, samplerate=22050, format='WAV') 
    audio_bytes_io.seek(0)
    
    return audio_bytes_io

st.title("Text-to-Speech Generator")

# Text input
text = st.text_input("Enter text:")

if st.button("Generate Speech"):
    if text:
        try:
            # Generate speech
            audio_bytes_io = generate_speech(text)
            
            # Provide the audio for playback
            st.audio(audio_bytes_io, format='audio/wav')
            st.success("Speech generated successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter some text.")
