import mdp
import numpy
import pylab as plt
from image_tools import *

"""Performs a PCA on natural image, white noise, and filtered
white noise patches in vector representation. Uses 5000 40 x 40 patches and
analyzes the first 25 basis vectors."""

image_path  = "./images/"
img_type    = "tiff"

numberPatches = 5
patchSize     = 40
patches       = []

for i in range(numberPatches):
    currentImg = get_random_image(image_path, img_type)
    currentImg = load_image(currentImg)
    
    patch = get_random_patch(currentImg, patchSize)
    patch = np.array(patch)
    patch = patch.reshape(patchSize**2,1)
    
    patches = np.concatenate((patches, norm_patch(patch)))
    
#patches = patches.reshape(1,)
print patches

#y = mdp.pca(patches)

