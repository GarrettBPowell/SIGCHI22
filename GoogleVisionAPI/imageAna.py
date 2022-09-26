from PIL import Image
from os import listdir
from os.path import isfile, join
import io
import os

def getFrames(fileName, gif, num_key_frames):
    with Image.open(gif) as im:
        for i in range(num_key_frames):
            im.seek(im.n_frames // num_key_frames * i)
            im.save(os.path.abspath('resources/splitGifs/{}-{}.png'.format(fileName, i)))
            print(i)