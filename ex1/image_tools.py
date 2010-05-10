
import Image
import numpy as np

def load_image(path):
    im = Image.open(path)
    im_ar = np.array(im.getdata())
    return np.reshape(im_ar, (im.size[1], im.size[0]))

def add_noise(im, sigma):
    noise = np.random.randn(np.shape(im)[0], np.shape(im)[1]) * sigma
    return im + noise
