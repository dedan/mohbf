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

def get_random_patch(image, size=None):
    """Returns a random n-by-n patch of an image."""
    if size == None:
        maxSize     = np.min(np.shape(image))
        patchSize   = np.random.randint(1, maxSize)
    else: patchSize   = size

    xInd        = np.random.randint(1, np.shape(image)[0]-patchSize)
    yInd        = np.random.randint(1, np.shape(image)[1]-patchSize)
    return image[xInd:xInd+patchSize, yInd:yInd+patchSize]

def norm_patch(patch):
    """Normalizes a patch to zero mean and unitary variance."""
    return (patch-np.mean(patch))/np.std(patch)

def norm_patch_set(patch_set):
    """normalize a set of patches"""
    arr        = np.array(patch_set)
    var        = np.std(arr, axis=0)
    mean_patch = np.mean(arr, axis=0)
    return [(patch-mean_patch)/var for patch in patch_set]        




