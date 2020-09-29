from gtts import gTTS
import os
tts = gTTS(text="Want to start a blog and make a career as a blogger?", lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")


