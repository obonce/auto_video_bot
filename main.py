#!/usr/bin/python

from classes.speech_recognize import VideoPixySpeechRecognition
from classes.fetch_images import VideoPixyImageFetcher
from classes.image_text import VideoPixyTextOnImage
from classes.video_encoder import VideoPixyVideoEncoder
import sys


class VideoPixyMain:

    def __init__(self):
        self.__videoPixySpeechRecognition = VideoPixySpeechRecognition()
        self.__videoPixyImageFetcher = VideoPixyImageFetcher()
        self.__videoPixyTextOnImage = VideoPixyTextOnImage()
        self.__videoPixyVideoEncoder = VideoPixyVideoEncoder()

    def executeJob(self):
        # Step 1: We will fetch sentences in array format from audio file
        sentences = self.__videoPixySpeechRecognition.convertLargeAudioToText(
            "storage/dcuo_gamer.wav")

        # Step 2: We will fetch images from the sentences                                                                                                                                                    'And how to play dc universe online. ')], [('audio-chunks/chunk4.wav', 'The first we have superman and the second we have batman. ')], [('audio-chunks/chunk5.wav', 'In anyways so in this tutorial i will be teaching you how to play dc universe online. ')]]
        imagesJson = self.__videoPixyImageFetcher.fetchImagesFromSentences(
            sentences)

        # Step 3; We will put sentences below the images as memes
        if imagesJson:
            finalClipsDict = self.__videoPixyTextOnImage.addTextToDownloadedImages(
                imagesJson)

        # Step 4: We will combine the audio and images into video with animation effects
        if finalClipsDict:
            self.__videoPixyVideoEncoder.combineImages(finalClipsDict)


videopixy = VideoPixyMain()
videopixy.executeJob()
