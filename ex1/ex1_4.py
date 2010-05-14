import numpy as np
from image_tools import *
import pylab as pl
from scipy.signal import convolve2d

"""Generates 500 16 x 16 pixel image patches from the image data base 
and normalizes the set."""

numberPatches = 3
patchSize = 16

image_path  = "./images/"
img_type    = "tiff"

sigma = 1000
kernelSize = 9
kernel = np.ones((kernelSize, kernelSize)) / (kernelSize ** 2)
normedPatches = []
noisePatches = []
filteredNoisePatches = []

for i in range (numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)
    
    patch = get_random_patch(currentImg, 16)
    
    noisyPatch = add_noise(patch, sigma)

    noise = np.random.randn(patchSize, patchSize) * sigma
    filteredNoise  = convolve2d(noise, kernel, 'same')
    filteredNoisePatch = patch + filteredNoise
    
    normedPatches.append(norm_patch(patch))
    noisePatches.append(norm_patch(noisyPatch))
    filteredNoisePatches.append(norm_patch(filteredNoisePatch))

pl.figure()
pl.subplot(1,3,1)
pl.imshow(normedPatches[1])
pl.gray()
pl.subplot(1,3,2)
pl.imshow(noisePatches[1])
pl.gray()
pl.subplot(1,3,3)
pl.imshow(filteredNoisePatches[1])
pl.gray()
pl.show()

    

     


    
