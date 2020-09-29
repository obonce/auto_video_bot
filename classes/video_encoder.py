
from moviepy.editor import *

import sys


class VideoPixyVideoEncoder:
    def __init__(self):
        pass

    def combineImages(self, clips):
        finalVideoClips = []
        for clip in clips:
            videoClip = self._setClipData(clip.get("audio_file"), clip.get(
                "image_text"), clip.get("image_path"))

            finalVideoClips.append(videoClip)

        self.makeVideo(finalVideoClips)

    def _setClipData(self, audioFile, imageText, imagePath):

        if audioFile and imageText and imagePath:

            # Import the audio(Insert to location of your audio instead of audioClip.mp3)
            audio = AudioFileClip(audioFile)
            # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
            clip = ImageClip(imagePath).set_duration(
                audio.duration).fx(vfx.fadein, 0.5)
            # Set the audio of the clip
            clip = clip.set_audio(audio)

            return clip

    def makeVideo(self, clips):
        final_clip = concatenate_videoclips(clips,
                                            method="compose")
        final_clip.write_videofile('final.mp4',
                                   codec='libx264',
                                   audio_codec='aac',
                                   temp_audiofile='temp-audio.m4a',
                                   remove_temp=True,
                                   fps=60,
                                   )


x = VideoPixyVideoEncoder()
