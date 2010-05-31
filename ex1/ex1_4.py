import numpy as np
from image_tools import *
import pylab as pl
from scipy.signal import convolve2d

"""Generates 500 16 x 16 pixel image patches from the image data base,
500 16 x 16 pixel white noise patches, 500 16 x 16 pixel patches of filtered noise 
and normalizes each set."""

numberPatches = 500
patchSize = 16

image_path  = "./images/"
img_type    = "tiff"

sigma = 100
kernelSize = 9
kernel = np.ones((kernelSize, kernelSize)) / (kernelSize ** 2)
patches = []
noisePatches = []
filteredNoisePatches = []

for i in range (numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)
    
    patch = get_random_patch(currentImg, patchSize)
    noisePatch = np.random.randn(patchSize, patchSize) * sigma
    filteredNoisePatch  = convolve2d(noisePatch, kernel, 'same')
    
    patches.append(patch)
    noisePatches.append(noisePatch)
    filteredNoisePatches.append(filteredNoisePatch)

patches = norm_patch_set(patches)
noisePatches = norm_patch_set(noisePatches)
filteredPatches = norm_patch_set(filteredNoisePatches)

pl.rcParams['image.interpolation'] = 'nearest'
pl.figure()
pl.subplot(1,3,1)
pl.imshow(patches[1])
pl.gray()
pl.subplot(1,3,2)
pl.imshow(noisePatches[1])
pl.gray()
pl.subplot(1,3,3)
pl.imshow(filteredNoisePatches[1])
pl.gray()
pl.show()

    

     


    
