#python -m pip install torch
#python -r pip install transformers

#python -m pip install chromadb
# nếu dùng OpenAI embeddings:
#python -m pip install openai
# hoặc dùng sentence-transformers (free, local):

from transformers import pipeline

# Load a pre-trained TTS model
pipe = pipeline("text-to-speech", model="suno/bark-small")

# Input text
text = "Hello Truong, welcome to Hugging Face TTS!"

# Generate audio
speech = pipe(text)

# Save to file
with open("output.wav", "wb") as f:
    f.write(speech["audio"])

