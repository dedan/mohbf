
import Image
import numpy as np
import glob
import random

def load_image(path):
    """Loads an image form specified path and converts it to a matrix."""
    im = Image.open(path)
    im_ar = np.array(im.getdata())
    return np.reshape(im_ar, (im.size[1], im.size[0]))

def add_noise(im, sigma):
    """Adds gaussian noise with a variance of sigma to an image."""
    noise = np.random.randn(np.shape(im)[0], np.shape(im)[1]) * sigma
    return im + noise

def get_random_image(path, im_type):
    """Returns a random image from database."""
    return random.choice(glob.glob(path +"*." +im_type))

def get_random_patch(image):
    """Returns a random n-by-n patch of an image."""
    maxSize     = np.min(np.shape(image))
    patchSize   = np.random.randint(1, maxSize)
    xInd        = np.random.randint(1, np.shape(image)[0]-patchSize)
    yInd        = np.random.randint(1, np.shape(image)[1]-patchSize)
    return image[xInd:xInd+patchSize, yInd:yInd+patchSize]

def norm_patch(patch):
    """Normalizes a patch to zero mean and unitary variance."""
    meanPatch = np.mean(patch)
    varPatch  = np.std(patch)
    return (patch-meanPatch)/varPatch
