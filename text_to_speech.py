# This text to speech converter uses microsoft/speecht5_tts model and it is not on the streamlit

# pip install datasets
# pip install soundfile

from transformers import AutoProcessor, AutoModelForTextToSpectrogram
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

processor = AutoProcessor.from_pretrained("microsoft/speecht5_tts")
model = AutoModelForTextToSpectrogram.from_pretrained("microsoft/speecht5_tts")

from transformers import pipeline

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# You can replace this embedding with your own as well.

speech = synthesiser("This generative ai course is so good that it helps me to build amazing chatbots uisng some models", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("speech2.wav", speech["audio"], samplerate=speech["sampling_rate"])
