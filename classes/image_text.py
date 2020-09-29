import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps

import sys


class VideoPixyTextOnImage:

    def __init__(self):
        pass

    def addTextToDownloadedImages(self, imagesJson):
        finalClips = []
        for audioFile, imageData in imagesJson:
            for imageText, imagePath in imageData[0].items():
                self.addTextToImage(imageText, imagePath[0])
                finalClips.append(
                    {"audio_file": audioFile, "image_text": imageText, "image_path": imagePath[0]})

        return finalClips

    def addTextToImage(self, imageText, filename):
        img = Image.open(filename)

        # borders
        img = ImageOps.expand(img, border=10, fill='white')
        img = ImageOps.expand(img, border=100, fill='black')

        imageSize = img.size

        fontSize = int(imageSize[1]/12)
        fontName = "/Library/Fonts/Impact.ttf"
        font = ImageFont.truetype(fontName, fontSize)
        bottomTextSize = font.getsize(imageText)

        while bottomTextSize[0] > imageSize[0]-20:
            fontSize = fontSize - 1
            font = ImageFont.truetype(fontName, fontSize)
            bottomTextSize = font.getsize(imageText)

        # find bottom centered position for bottom text
        bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
        bottomTextPositionY = imageSize[1] - bottomTextSize[1]
        bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)
        draw = ImageDraw.Draw(img)

        # draw outlines
        # there may be a better way
        outlineRange = int(fontSize/15)
        for x in range(-outlineRange, outlineRange+1):
            for y in range(-outlineRange, outlineRange+1):
                draw.text(
                    (bottomTextPosition[0]+x, bottomTextPosition[1]+y), imageText, (0, 0, 0), font=font)

        draw.text(bottomTextPosition, imageText, (255, 255, 255), font=font)

        img.save(filename)
