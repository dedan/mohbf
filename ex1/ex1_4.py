import numpy as np
from image_tools import *
import pylab as pl

"""Generate 500 16 × 16 pixel image patches from the image data base and normalize
the set."""

numberPatches = 500
patchSize = 16

image_path  = "./images/"
img_type    = "tiff"

normedPatches = []

for i in range (numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)

    patch = get_random_patch(currentImg, 16)
    normedPatches.append(norm_patch(patch))


    
