from PIL import Image
from os import listdir
from os.path import isfile, join
import io
import os
import datetime

def getXAmountOfFrames(fileName, gif, num_key_frames):
    with Image.open(gif) as im:
        for i in range(num_key_frames):
            im.seek(im.n_frames // num_key_frames * i)
            im.save(os.path.abspath('resources/splitGifs/{}-{}.png'.format(fileName, i)))

def getFirstAndMiddleFrame(fileName, gif):
    ct = datetime.datetime.now()
    with Image.open(gif) as im:
        im.seek(0)
        im.save(os.path.abspath('resources/splitGifs/{}-{}-first-{}.png'.format(fileName, 0, ct.timestamp())))
        try:
            midPoint = im.n_frames // 2
            if(midPoint > 0):
                im.seek(midPoint)
                im.save(os.path.abspath('resources/splitGifs/{}-{}-middle-{}.png'.format(fileName, midPoint, ct.timestamp())))
        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("EXCEPTION")
            print("Failed to get midpoint frame. You most likely did not pass a gif. \n\n")
            print("File Name: {}\nFile Path: {}\n********************************".format(fileName, gif))
