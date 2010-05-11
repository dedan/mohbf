
import Image
import numpy as np
import glob
import random

def load_image(path):
    im = Image.open(path)
    im_ar = np.array(im.getdata())
    return np.reshape(im_ar, (im.size[1], im.size[0]))

def add_noise(im, sigma):
    noise = np.random.randn(np.shape(im)[0], np.shape(im)[1]) * sigma
    return im + noise

def get_random_image(path, im_type):
    return random.choice(glob.glob(path +"*." +im_type))

def get_random_patch(image):
    """Returns a random n-by-n patch of an image."""
    imgSize = np.sort(np.shape(image))

    patchSize = np.random.randint(1, imgSize[0])
    xInd = np.random.randint(1, imgSize[0]-patchSize)
    yInd = np.random.randint(1, imgSize[0]-patchSize)

    patch = np.zeros((patchSize,patchSize))

    for i in np.arange(xInd,xInd+patchSize,1):
        for j in np.arange(yInd,yInd+patchSize,1):
            patch[i-xInd,j-yInd] = image[i,j]

    return patch
