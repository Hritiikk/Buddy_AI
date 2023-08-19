# gtts test
# pip install gTTS
from gtts import gTTS
import os

hindi_text = "नमस्ते, यह एक परीक्षण है।"
audio = gTTS(text=hindi_text, lang="hi")
audio.save("output.mp3")
os.system("start output.mp3")
