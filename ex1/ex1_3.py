import pylab as plt
from image_tools import *
import numpy as np

image_path  = "./images/"
img_type    = "tiff"
patch_size  = 16
n_patches   = 2
plt.rcParams['image.interpolation'] = 'nearest'

"""Loads a rando image from database, extracts and nomalizes a random patch of it
and plots both."""

# load random image
chosen_one  = get_random_image(image_path, img_type)
rand_img    = load_image(chosen_one)
plt.imshow(rand_img)
plt.gray()
plt.title(chosen_one)

# get random patch and norm it
patch       = get_random_patch(rand_img)
normedPatch = norm_patch(patch)
print np.mean(normedPatch)
print np.std(normedPatch)
plt.figure()
plt.imshow(normedPatch)

# norm a set of patches
patch_set = [get_random_patch(rand_img, patch_size) for i in range(n_patches)]
normed_patch_set = norm_patch_set(patch_set)

print np.mean(np.array(normed_patch_set), axis=0)
print np.std(np.array(normed_patch_set), axis=0)
plt.show()

