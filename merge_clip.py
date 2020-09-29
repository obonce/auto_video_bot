from moviepy.editor import *


# Import the audio(Insert to location of your audio instead of audioClip.mp3)
audio1 = AudioFileClip("audio1.wav")
# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
clip1 = ImageClip("video1.jpg").set_duration(audio1.duration)
# Set the audio of the clip
clip1 = clip1.set_audio(audio1)


# Import the audio(Insert to location of your audio instead of audioClip.mp3)
audio2 = AudioFileClip("audio2.wav")
# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
clip2 = ImageClip("video2.png").set_duration(
    audio2.duration).set_start(clip1.end-1).fx(vfx.fadein, 0.5)
# Set the audio of the clip
clip2 = clip2.set_audio(audio2)


final_clip = concatenate_videoclips([clip1, clip2],
                                    method="compose")
final_clip.write_videofile('final.mp4',
                           codec='libx264',
                           audio_codec='aac',
                           temp_audiofile='temp-audio.m4a',
                           remove_temp=True,
                           fps=60,
                           )
