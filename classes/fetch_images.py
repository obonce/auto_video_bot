from google_images_download import google_images_download

import ssl
import sys


class VideoPixyImageFetcher:
    def __init__(self):
        print('Init image fetcher library')

    def fetchImagesFromSentences(self, sentences):
        responses = []
        for sentence in sentences:
            for audioFile, sentenceText in sentence:
                responses.append(
                    (audioFile, self.__downloadImages(sentenceText)))

        return responses

    def __downloadImages(self, query):
        context = ssl._create_unverified_context()
        response = google_images_download.googleimagesdownload()
        # keywords is the search query
        # format is the image file format
        # limit is the number of images to be downloaded
        # print urs is to print the image file url
        # size is the image size which can
        # be specified manually ("large, medium, icon")
        # aspect ratio denotes the height width ratio
        # of images to download. ("tall, square, wide, panoramic")
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": True,
                     "usage_rights": "labeled-for-reuse-with-modifications",
                     "output_directory": "storage/google_images",
                     "image_directory": "video_id_1"}
        # "size": "large"}
        # "aspect_ratio": "panoramic" }
        '''
            I've played around with different parameters
            some yeild resuts and others don't. It can also depend on the searched query
            '''

        try:
            return response.download(arguments)

        # Handling File NotFound Error
        except FileNotFoundError:
            arguments = {"keywords": query,
                         "format": "jpg",
                         "limit": 1,
                         "print_urls": True,
                         "size": "medium",
                         "output_directory": "storage/google_images",
                         "image_directory": "video_id_1"}

            # Providing arguments for the searched query
            try:
                # Downloading the photos based
                # on the given arguments
                response.download(arguments)
            except:
                pass
